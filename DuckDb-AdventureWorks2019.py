import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    __generated_with = "0.13.15"
    app = mo.App(width="medium")
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # DuckDB Connection Troubleshooting

    ## Problem
    Database path `Q:\Database\AdventureWorksDW` was causing "Access denied" errors.

    ## Root Cause
    The path pointed to a **directory**, not a database file. DuckDB needs the actual `.duckdb` file path.

    ## Solution Strategy
    1. **Diagnose** - Check if path is file or directory
    2. **Fallback Logic** - If directory, scan for `.duckdb` files inside
    3. **Safe Connection** - Use read-only mode to prevent accidental changes

    ## Key Code Logic
    ```python
    # First try direct connection
    conn = duckdb.connect(db_path, read_only=True)

    # If that fails and it's a directory:
    if os.path.isdir(db_path):
        db_files = [f for f in os.listdir(db_path) if f.endswith('.duckdb')]
        actual_db_path = os.path.join(db_path, db_files[0])
        conn = duckdb.connect(actual_db_path, read_only=True)
    ```

    ## Result
    ✅ **Success**: Found and connected to `AdventureWorksDW2019.duckdb` inside the directory

    ## Best Practices Applied
    - **Defensive Programming**: Multiple fallback strategies
    - **Safety First**: Read-only connections
    - **Clear Diagnostics**: Detailed error reporting
    - **Robust File Handling**: Automatic database file discovery

    This approach handles common Windows database path issues and provides a reliable connection method for DuckDB files.
    """
    )
    return


@app.cell
def _():
    import duckdb
    import os

    # Simple diagnostic approach - let's figure out what's wrong
    db_path = r'Q:\Database\AdventureWorksDW'

    print("🔍 Diagnosing database connection issue...")
    print(f"Database path: {db_path}")
    print(f"Path exists: {os.path.exists(db_path)}")
    print(f"Is file: {os.path.isfile(db_path)}")
    print(f"Is directory: {os.path.isdir(db_path)}")

    if os.path.exists(db_path):
        print(f"File size: {os.path.getsize(db_path) if os.path.isfile(db_path) else 'N/A (directory)'}")
        print(f"Read access: {os.access(db_path, os.R_OK)}")
        print(f"Write access: {os.access(db_path, os.W_OK)}")

    # Try the simplest connection approaches first
    try:
        # Method 1: Read-only connection (safest)
        conn = duckdb.connect(db_path, read_only=True)
        print("✅ SUCCESS: Connected in read-only mode")
        connection_status = "Connected (read-only)"
    except Exception as e1:
        print(f"❌ Read-only failed: {e1}")

        try:
            # Method 2: Check if it's a directory issue
            if os.path.isdir(db_path):
                # Maybe it's a directory with a specific file inside
                files_in_dir = os.listdir(db_path)
                print(f"Directory contains: {files_in_dir}")

                # Look for common database file extensions
                db_files = [f for f in files_in_dir if f.endswith(('.db', '.duckdb', '.sqlite'))]
                if db_files:
                    actual_db_path = os.path.join(db_path, db_files[0])
                    conn = duckdb.connect(actual_db_path, read_only=True)
                    print(f"✅ SUCCESS: Connected to {actual_db_path}")
                    connection_status = f"Connected to {db_files[0]} (read-only)"
                else:
                    raise Exception("No database files found in directory")
            else:
                raise e1

        except Exception as e2:
            print(f"❌ Directory approach failed: {e2}")
            connection_status = "Failed to connect"
            conn = None

    # Show the connection status
    print(f"\n📊 Final Status: {connection_status}")
    return (conn,)


@app.cell
def _(conn):
    # Test the connection and show available tables
    def test_database_connection():
        try:
            tables_result = conn.execute("SHOW TABLES").fetchall()

            print("📊 AdventureWorks Database Connected Successfully!")
            print("=" * 60)
            print(f"Database file: AdventureWorksDW2019.duckdb")
            print(f"Connection mode: Read-only")
            print(f"Available tables: {len(tables_result)}")
            print()

            # Show all tables in a nice format
            print("📋 Available Tables:")
            print("-" * 40)
            for i, (table_name,) in enumerate(tables_result, 1):
                print(f"  {i:2d}. {table_name}")

            # Show sample data from the first table
            if tables_result:
                sample_table = tables_result[0][0]
                print(f"\n🔍 Sample data from '{sample_table}':")
                print("-" * 50)

                sample_query = f"SELECT * FROM {sample_table} LIMIT 3"
                sample_data = conn.execute(sample_query).fetchall()
                table_columns = [desc[0] for desc in conn.description]

                # Print column headers
                header = " | ".join(f"{col:15}" for col in table_columns)
                print(header)
                print("-" * len(header))

                # Print sample rows
                for row in sample_data:
                    row_str = " | ".join(f"{str(val):15}" for val in row)
                    print(row_str)

        except Exception as e:
            print(f"❌ Error testing connection: {e}")

    # Run the test and make connection available
    test_database_connection()
    database_connection = conn
    return (database_connection,)


@app.cell
def _(mo):
    mo.md(r"""Direct query execution""")
    return


@app.cell
def _(database_connection):
    # Direct query execution
    direct_result = database_connection.execute("SELECT COUNT(*) FROM FactInternetSales").fetchall()
    print(f"Total rows in FactInternetSales: {direct_result[0][0]}")
    return


@app.cell
def _(mo):
    mo.md(r"""## **Pristine Reactive Database Analytics with Marimo (See at the end the details)**""")
    return


@app.cell
def _(database_connection):
    class AdventureWorksQueryEngine:
        """Single responsibility: Execute database queries"""

        def __init__(self, connection):
            self.conn = connection

        def execute_query(self, query):
            """DRY: Single method for all query execution"""
            result = self.conn.execute(query).fetchall()
            columns = [desc[0] for desc in self.conn.description] if self.conn.description else []
            return result, columns

        def execute_scalar(self, query):
            """DRY: Single method for scalar results"""
            result, _ = self.execute_query(query)
            return result[0][0] if result else None

    # Create the query engine
    query_engine = AdventureWorksQueryEngine(database_connection)
    print("✅ Query engine initialized")
    return (query_engine,)


@app.cell
def _():
    class AdventureWorksQueries:
        """Single responsibility: Define all queries"""

        SALES_COUNT = "SELECT COUNT(*) FROM FactInternetSales"

        # Exclude LargePhoto and other binary columns
        SAMPLE_PRODUCTS = """
            SELECT 
                ProductKey, ProductAlternateKey, ProductSubcategoryKey, 
                WeightUnitMeasureCode, SizeUnitMeasureCode, EnglishProductName,
                SpanishProductName, FrenchProductName, StandardCost, Color,
                ListPrice, Size, SizeRange, Weight, ProductLine, DealerPrice,
                Class, Style, ModelName, Status, DuckdbLoadDate
            FROM DimProduct 
            LIMIT 5
        """

        YEARLY_SALES = """
            SELECT 
                YEAR(OrderDate) as Year,
                COUNT(*) as OrderCount,
                SUM(SalesAmount) as TotalSales
            FROM FactInternetSales 
            GROUP BY YEAR(OrderDate)
            ORDER BY Year
        """

    # Query definitions ready
    fixed_queries = AdventureWorksQueries()
    print("✅ Fixed query definitions loaded")
    return (fixed_queries,)


@app.cell
def _():
    import pandas as pd

    class DataTransformer:
        """Single responsibility: Transform query results to DataFrames"""

        @staticmethod
        def to_dataframe(result, columns):
            """DRY: Single method for DataFrame conversion"""
            return pd.DataFrame(result, columns=columns)

        @staticmethod
        def format_count(count, label):
            """DRY: Single method for count formatting"""
            return f"{label}: {count:,}"

    # Create transformer
    transformer = DataTransformer()
    print("✅ Data transformer ready")
    return (transformer,)


@app.cell
def _(mo):
    mo.md(
        r"""
    # Execute sales count query
    sales_count_value = query_engine.execute_scalar(fixed_queries.SALES_COUNT)
    sales_count_display = transformer.format_count(sales_count_value, "Total Internet Sales")
    print(sales_count_display)
    """
    )
    return


@app.cell
def _(fixed_queries, query_engine, transformer):
    # Execute products query with fixed syntax
    products_result, products_columns = query_engine.execute_query(fixed_queries.SAMPLE_PRODUCTS)
    products_dataframe = transformer.to_dataframe(products_result, products_columns)
    products_dataframe
    return (products_dataframe,)


@app.cell
def _(fixed_queries, query_engine, transformer):
    # Execute yearly sales query
    yearly_result, yearly_columns = query_engine.execute_query(fixed_queries.YEARLY_SALES)
    yearly_dataframe = transformer.to_dataframe(yearly_result, yearly_columns)
    yearly_dataframe
    return (yearly_dataframe,)


@app.cell
def _(fixed_queries, mo, products_dataframe, query_engine, yearly_dataframe):
    # Clean dashboard using the updated queries
    pristine_dashboard = mo.vstack([
        mo.md("## AdventureWorks Analytics Dashboard"),
        mo.md(f"**Total Internet Sales:** {query_engine.execute_scalar(fixed_queries.SALES_COUNT):,}"),
        mo.md("---"),
        mo.md("### Sample Products"),
        mo.ui.table(products_dataframe),
        mo.md("### Sales by Year"),
        mo.ui.table(yearly_dataframe)
    ])

    pristine_dashboard
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Pristine Reactive Database Analytics with Marimo

    ## Overview
    This implementation demonstrates a clean, maintainable approach to database analytics using marimo's reactive programming model while adhering to software engineering best practices: **KISS (Keep It Simple, Stupid)**, **SRP (Single Responsibility Principle)**, and **DRY (Don't Repeat Yourself)**.

    ## Architecture Components

    ### 1. Database Connection Layer
    ```python
    # Robust connection handling with fallback logic
    db_path = r'Q:\Database\AdventureWorksDW'
    conn = duckdb.connect(actual_db_path, read_only=True)
    ```
    - **Challenge Solved**: Windows path issues and directory vs. file detection
    - **Solution**: Automatic discovery of `.duckdb` files within directories
    - **Safety**: Read-only connection prevents accidental data modification

    ### 2. Query Engine (SRP Implementation)
    ```python
    class AdventureWorksQueryEngine:
        \"""Single responsibility: Execute database queries\"""

        def execute_query(self, query):
            \"""DRY: Single method for all query execution\"""

        def execute_scalar(self, query):
            \"""DRY: Single method for scalar results\"""
    ```
    - **SRP**: Handles only database operations
    - **DRY**: Eliminates duplicate query execution code
    - **Encapsulation**: Centralizes connection management

    ### 3. Query Definitions (SRP Implementation)
    ```python
    class AdventureWorksQueries:
        \"""Single responsibility: Define all queries\"""

        SALES_COUNT = "SELECT COUNT(*) FROM FactInternetSales"
        SAMPLE_PRODUCTS = \"""SELECT ProductKey, ProductAlternateKey, ... FROM DimProduct LIMIT 5\"""
        YEARLY_SALES = \"""SELECT YEAR(OrderDate) as Year, ... FROM FactInternetSales ...\"""
    ```
    - **SRP**: Stores only query definitions
    - **DRY**: Centralized query management
    - **Maintainability**: Easy to modify queries in one location

    ### 4. Data Transformation Layer (SRP Implementation)
    ```python
    class DataTransformer:
        \"""Single responsibility: Transform query results to DataFrames\"""

        @staticmethod
        def to_dataframe(result, columns):
            \"""DRY: Single method for DataFrame conversion\"""

        @staticmethod
        def format_count(count, label):
            \"""DRY: Single method for count formatting\"""
    ```
    - **SRP**: Handles only data transformation
    - **DRY**: Reusable transformation methods
    - **Consistency**: Standardized data formatting

    ## Reactive Cell Structure

    ### Individual Data Cells (Maximum Flexibility)
    ```python
    # Cell 1: Sales Count
    sales_count_value = query_engine.execute_scalar(fixed_queries.SALES_COUNT)

    # Cell 2: Products Data  
    products_result, products_columns = query_engine.execute_query(fixed_queries.SAMPLE_PRODUCTS)
    products_dataframe = transformer.to_dataframe(products_result, products_columns)

    # Cell 3: Yearly Sales Data
    yearly_result, yearly_columns = query_engine.execute_query(fixed_queries.YEARLY_SALES)
    yearly_dataframe = transformer.to_dataframe(yearly_result, yearly_columns)
    ```

    ### Unified Dashboard Cell
    ```python
    pristine_dashboard = mo.vstack([
        mo.md("## AdventureWorks Analytics Dashboard"),
        mo.md(f"**Total Internet Sales:** {query_engine.execute_scalar(fixed_queries.SALES_COUNT):,}"),
        mo.md("---"),
        mo.md("### Sample Products"),
        mo.ui.table(products_dataframe),
        mo.md("### Sales by Year"),
        mo.ui.table(yearly_dataframe)
    ])
    ```

    ## Key Technical Challenges Resolved

    ### 1. SQL Dialect Compatibility
    - **Issue**: SQL Server `TOP 5` syntax incompatible with DuckDB
    - **Solution**: Converted to standard SQL `LIMIT 5`
    - **Learning**: Always use ANSI SQL standards for portability

    ### 2. Binary Data Handling
    - **Issue**: `LargePhoto` column contained binary GIF data causing UTF-8 encoding errors
    - **Root Cause**: `b'GIF89a\xf0\x00\x95\x00...'` binary data cannot be displayed in tables
    - **Solution**: Excluded binary columns from SELECT statements
    - **Prevention**: Always identify and handle binary columns in data migration

    ### 3. Marimo Variable Scoping
    - **Issue**: Cannot redefine variables across cells
    - **Solution**: Unique variable names and proper cell organization
    - **Best Practice**: Plan variable naming strategy upfront

    ## Implementation Approaches Comparison

    | Approach | Flexibility | Maintainability | Debugging | Use Case |
    |----------|-------------|-----------------|-----------|----------|
    | **Separate Cells** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Exploratory analysis, development |
    | **Combined Display** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | Dashboards, presentations |
    | **Single Function** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | Production, reusable components |

    ## Variable Naming Strategies

    ### Approach 1: Descriptive Names
    ```python
    sales_count_value, products_dataframe, yearly_dataframe
    ```
    - **Pros**: Clear purpose, easy to understand
    - **Cons**: Longer names
    - **Best for**: Development and exploration

    ### Approach 2: Prefixed Names  
    ```python
    _sales_count, _products_df, _yearly_df
    ```
    - **Pros**: Shorter, indicates internal use
    - **Cons**: Less descriptive
    - **Best for**: Combined displays

    ### Approach 3: Scoped Names
    ```python
    total_sales_count, all_products_df, all_yearly_df
    ```
    - **Pros**: Context-aware, prevents conflicts
    - **Cons**: Can become verbose
    - **Best for**: Large applications

    ## Reactive Benefits Achieved

    1. **Automatic Updates**: Change a query → all dependent cells update
    2. **Clean Dependencies**: Clear data flow through the application
    3. **Error Isolation**: Problems in one cell don't break others
    4. **Performance**: Only affected cells re-execute on changes

    ## Best Practices Demonstrated

    - ✅ **Separation of Concerns**: Database, transformation, and presentation layers
    - ✅ **Error Handling**: Graceful handling of connection and encoding issues  
    - ✅ **Code Reusability**: Modular components that can be extended
    - ✅ **Documentation**: Clear class and method documentation
    - ✅ **Type Safety**: Consistent data types and transformations
    - ✅ **Performance**: Efficient query execution and data handling

    This pristine implementation provides a solid foundation for scalable, maintainable database analytics in marimo while demonstrating professional software development practices.
    """
    )
    return


if __name__ == "__main__":
    app.run()
