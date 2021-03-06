"""
Env dataclass to load and hold all environment variables
"""

# Import libraries
import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path
from typing import Optional


@dataclass(frozen=True) # emulate immutability by passing frozen=True
class EnvVariables:
    """
    Loads all environment variables into a predefined set of properties
    """
    
    # load variables defined in <PROJECT_ROOT>/config/.env file into environment variables for local execution
    load_dotenv(dotenv_path=Path(__file__).parents[2] / ".env")

    tenant_id: Optional[str] = os.environ.get("TENANT_ID")
    subscription_id: Optional[str] = os.environ.get("SUBSCRIPTION_ID")
    resource_group: Optional[str] = os.environ.get("RESOURCE_GROUP")
    workspace_name: Optional[str] = os.environ.get("WORKSPACE_NAME")
    experiment_name: Optional[str] = os.environ.get("EXPERIMENT_NAME")
    data_dir: Optional[str] = os.environ.get("DATA_DIR")
    datastore_target_dir: Optional[str] = os.environ.get("DATASTORE_TARGET_DIR")
    src_dir: Optional[str] = os.environ.get("SRC_DIR")
    sp_app_id: Optional[str] = os.environ.get("SP_APP_ID")
    sp_app_secret: Optional[str] = os.environ.get("SP_APP_SECRET")
    vm_size: Optional[str] = os.environ.get("AML_COMPUTE_CLUSTER_GPU_SKU")
    compute_name: Optional[str] = os.environ.get("AML_COMPUTE_CLUSTER_NAME")
    # vm_priority: Optional[str] = os.environ.get(
    #     "AML_CLUSTER_PRIORITY", "lowpriority"
    # )  # NOQA: E501
    # min_nodes: int = int(os.environ.get("AML_CLUSTER_MIN_NODES", 0))
    # max_nodes: int = int(os.environ.get("AML_CLUSTER_MAX_NODES", 4))
    build_id: Optional[str] = os.environ.get("BUILD_ID")
    pipeline_name: Optional[str] = os.environ.get("TRAINING_PIPELINE_NAME")
    # conda_env_directory: Optional[str] = os.environ.get("CONDA_ENV_DIR")
    # sources_directory_train: Optional[str] = os.environ.get(
    #     "SOURCES_DIR_TRAIN"
    # )  # NOQA: E501
    pipeline_train_script_path: Optional[str] = os.environ.get("PIPELINE_TRAIN_SCRIPT_PATH")
    pipeline_evaluate_script_path: Optional[str] = os.environ.get(
        "PIPELINE_EVALUATE_SCRIPT_PATH"
    )  # NOQA: E501
    pipeline_register_script_path: Optional[str] = os.environ.get(
        "PIPELINE_REGISTER_SCRIPT_PATH"
    )  # NOQA: E501
    model_name: Optional[str] = os.environ.get("MODEL_NAME")
    # model_version: Optional[str] = os.environ.get("MODEL_VERSION")
    # image_name: Optional[str] = os.environ.get("IMAGE_NAME")
    # db_cluster_id: Optional[str] = os.environ.get("DB_CLUSTER_ID")
    # score_script: Optional[str] = os.environ.get("SCORE_SCRIPT")
    build_uri: Optional[str] = os.environ.get("BUILD_URI")
    dataset_name: Optional[str] = os.environ.get("DATASET_NAME")
    datastore_name: Optional[str] = os.environ.get("DATASTORE_NAME")
    dataset_version: Optional[str] = os.environ.get("DATASET_VERSION")
    pipeline_run_evaluation: Optional[str] = os.environ.get("PIPELINE_RUN_EVALUATION", "true")
    pipeline_allow_run_cancel: Optional[str] = os.environ.get(
        "PIPELINE_ALLOW_RUN_CANCEL", "true"
    ) # NOQA: E501
    aml_train_env_name: Optional[str] = os.environ.get("AML_TRAIN_ENV_NAME")
    aml_train_env_conda_file_path: Optional[str] = os.environ.get(
        "AML_TRAIN_ENV_CONDA_FILE_PATH", "environments/conda/training_environment.yml"
    )
    aml_train_env_rebuild: Optional[bool] = os.environ.get(
        "AML_TRAIN_ENV_REBUILD", "false"
    ).lower().strip() == "true"

    # use_gpu_for_scoring: Optional[bool] = os.environ.get(
    #     "USE_GPU_FOR_SCORING", "false"
    # ).lower().strip() == "true"
    # aml_env_score_conda_dep_file: Optional[str] = os.environ.get(
    #     "AML_ENV_SCORE_CONDA_DEP_FILE", "conda_dependencies_scoring.yml"
    # )
    # aml_env_scorecopy_conda_dep_file: Optional[str] = os.environ.get(
    #     "AML_ENV_SCORECOPY_CONDA_DEP_FILE", "conda_dependencies_scorecopy.yml"
    # )
    # vm_size_scoring: Optional[str] = os.environ.get(
    #     "AML_COMPUTE_CLUSTER_CPU_SKU_SCORING"
    # )
    # compute_name_scoring: Optional[str] = os.environ.get(
    #     "AML_COMPUTE_CLUSTER_NAME_SCORING"
    # )
    # vm_priority_scoring: Optional[str] = os.environ.get(
    #     "AML_CLUSTER_PRIORITY_SCORING", "lowpriority"
    # )
    # min_nodes_scoring: int = int(
    #     os.environ.get("AML_CLUSTER_MIN_NODES_SCORING", 0)
    # )  # NOQA: E501
    # max_nodes_scoring: int = int(
    #     os.environ.get("AML_CLUSTER_MAX_NODES_SCORING", 4)
    # )  # NOQA: E501
    # rebuild_env_scoring: Optional[bool] = os.environ.get(
    #     "AML_REBUILD_ENVIRONMENT_SCORING", "false"
    # ).lower().strip() == "true"
    # scoring_datastore_storage_name: Optional[str] = os.environ.get(
    #     "SCORING_DATASTORE_STORAGE_NAME"
    # )
    # scoring_datastore_access_key: Optional[str] = os.environ.get(
    #     "SCORING_DATASTORE_ACCESS_KEY"
    # )
    # scoring_datastore_input_container: Optional[str] = os.environ.get(
    #     "SCORING_DATASTORE_INPUT_CONTAINER"
    # )
    # scoring_datastore_input_filename: Optional[str] = os.environ.get(
    #     "SCORING_DATASTORE_INPUT_FILENAME"
    # )
    # scoring_datastore_output_container: Optional[str] = os.environ.get(
    #     "SCORING_DATASTORE_OUTPUT_CONTAINER"
    # )
    # scoring_datastore_output_filename: Optional[str] = os.environ.get(
    #     "SCORING_DATASTORE_OUTPUT_FILENAME"
    # )
    # scoring_dataset_name: Optional[str] = os.environ.get(
    #     "SCORING_DATASET_NAME"
    # )  # NOQA: E501
    # scoring_pipeline_name: Optional[str] = os.environ.get(
    #     "SCORING_PIPELINE_NAME"
    # )  # NOQA: E501
    # aml_env_name_scoring: Optional[str] = os.environ.get(
    #     "AML_ENV_NAME_SCORING"
    # )  # NOQA: E501
    # aml_env_name_score_copy: Optional[str] = os.environ.get(
    #     "AML_ENV_NAME_SCORE_COPY"
    # )  # NOQA: E501
    # batchscore_script_path: Optional[str] = os.environ.get(
    #     "BATCHSCORE_SCRIPT_PATH"
    # )  # NOQA: E501
    # batchscore_copy_script_path: Optional[str] = os.environ.get(
    #     "BATCHSCORE_COPY_SCRIPT_PATH"
    # )  # NOQA: E501
    custom_vision_endpoint: Optional[str] = os.environ.get("CUSTOM_VISION_ENDPOINT")
    custom_vision_training_key: Optional[str] = os.environ.get("CUSTOM_VISION_TRAINING_KEY")
    custom_vision_prediction_key: Optional[str] = os.environ.get("CUSTOM_VISION_PREDICTION_KEY")
    custom_vision_prediction_resource_id: Optional[str] = os.environ.get("CUSTOM_VISION_PREDICTION_RESOURCE_ID")
    custom_vision_project_name: Optional[str] = os.environ.get("CUSTOM_VISION_PROJECT_NAME")
    custom_vision_publish_iteration_name: Optional[str] = os.environ.get("CUSTOM_VISION_PUBLISH_ITERATION_NAME")
