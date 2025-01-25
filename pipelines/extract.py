import pathlib
import argparse
import dlt.pipeline
from src.api.client import UpbankClient


def load_upbank(config_path: pathlib.Path, destination: str):
    """
    Load data from the Upbank API and run the pipeline.

    Args:
        config_path (pathlib.Path): Path to the configuration file.
        :param config_path:
        :param destination:
    """

    # Create an Upbank Client
    upbank = UpbankClient()

    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name="upbank",
        destination=destination,
        dataset_name="upbank",
        progress=dlt.progress.alive_progress(),
    )

    # Run the pipeline
    upbank_source = upbank.get_source(path=config_path)

    if destination == 'filesystem':
        pipeline.run(upbank_source, table_format="delta")

    elif destination == "postgres":
        pipeline.run(upbank_source)

    else:
        raise ValueError(f"Unsupported destination: {destination}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser('Load data from the Upbank API', add_help=True)
    parser.add_argument('-d', '--destination', type=str, default='postgres', help='Destination to load data to')
    args = parser.parse_args()

    # Determine the project root directory
    project_root = pathlib.Path(__file__).resolve().parents[1]

    # Define the configuration directory and file path
    config_dir = project_root / "config"
    config_file = config_dir / "upbank.yaml"

    # Load upbank data using the specified configuration file
    load_upbank(config_file, destination=args.destination)
