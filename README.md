# UpBank Client 🚀

A **data ingestion pipeline** built with [dlt](https://dlthub.com/) to extract transaction data from **Up Bank** and load it into a destination such as **PostgreSQL, Snowflake, or other supported databases**.

## Features

👉 Extracts transactions from the [Up Banking API](https://developer.up.com.au/).
👉 Supports multiple destinations like **PostgreSQL, Snowflake, and more**.
👉 Uses **dlt** for seamless extraction, transformation, and loading (ETL).
👉 Automates historical and incremental data loads.

## Installation

Ensure you have Python 3.8+ installed, then install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

Before running the pipeline, you need an **Up Bank API Token**:

1. Visit [Up's API page](https://api.up.com.au).
2. Follow the steps to generate a **Personal Access Token**.
3. Store this token in your environment:

```bash
export SOURCES__UPBANK__TOKEN="your_upbank_token"
```

Alternatively, you can create a `.env` file:

```ini
SOURCES__UPBANK__TOKEN=your_upbank_token
```

## Usage

### Run the ETL Pipeline

Run the pipeline to extract transactions and load them into a configured destination:

```bash
python pipelines/extract.py
```

### Configure Your Destination

This pipeline supports multiple destinations via **dlt**. Configure the target in `.dlt/secrets.toml`:

#### PostgreSQL Example

```toml
[destination.postgres.credentials]
host = "localhost"
port = 5432
user = "your_user"
password = "your_password"
database = "your_database"
```

#### Snowflake Example

```toml
[destination.snowflake.credentials]
account = "your_account"
user = "your_user"
password = "your_password"
database = "your_database"
warehouse = "your_warehouse"
```

### Running the Pipeline with a Specific Destination

Specify the destination when running the script:

```bash
python pipelines/extract.py --destination postgres
```

or

```bash
python pipelines/extract.py --destination snowflake
```

## Data Model

The extracted data includes:

- **Transactions**: Amount, category, description, status, etc.
- **Accounts**: Account name, balance, type (savings/spending), etc.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.

---

🚀 *Built with ❤️ using dlt for automated data ingestion.*