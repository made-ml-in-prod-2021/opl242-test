import pytest
import sys
sys.path.append("dags")


# -----------------------------------------------------------------------------
def test_dag_bag_import(dag_bag):
    assert dag_bag.dags is not None
    assert dag_bag.import_errors == {}


# -----------------------------------------------------------------------------
@pytest.mark.parametrize("task_name,n_tasks", [
    ("01_generate_data", 1),
    ("02_train_model_pipeline", 4),
    ("03_inference", 1),
])
def test_dags_load(dag_bag, task_name, n_tasks):
    assert task_name in dag_bag.dags
    assert n_tasks == len(dag_bag.dags[task_name].tasks)

  
# -----------------------------------------------------------------------------
@pytest.mark.parametrize("task_name,structure", [
    ("01_generate_data", {
        "Generate_data": [],
    }),
    ("02_train_model_pipeline", {
        "waiting_for_data": ["docker-airflow-preprocess"],
        "waiting_for_target": ["docker-airflow-preprocess"],
        "docker-airflow-preprocess": ["docker-airflow-split"],
        "docker-airflow-split": ["docker-airflow-train"],
        "docker-airflow-train": ["docker-airflow-eval"],
        "docker-airflow-eval": [],
    }),
    ("03_inference", {
        "waiting_for_data": ["docker-airflow-predict"],
        "waiting_for_target": ["docker-airflow-predict"],
        "docker-airflow-predict": [],
    }),
])
def test_dags_data_structure(dag_bag, task_name, structure):
    dag = dag_bag.dags[task_name]
    for name, task in dag.task_dict.items():
        assert set(structure[name]) == task.downstream_task_ids  
 