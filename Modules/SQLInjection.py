from core.modules import BaseClass


class SQLInjection(BaseClass):

    name = "SQL Injection"

    severity = "High"

    functions_prefix = ""

    functions = [

        # Native MySQL(i) Injection
        "(?<![^\s+(])mysql_query",
        "(?<![^\s+(])mysqli_multi_query",
        "(?<![^\s+(])mysqli_send_query",
        "(?<![^\s+(])mysqli_master_query",
        "(?<![^\s+(])mysql_unbuffered_query",
        "(?<![^\s+(])mysql_db_query",
        "mysqli::real_query",
        "mysqli_real_query",
        "mysqli::query",
        "mysqli_query",

        # PostgreSQL Injection
        "(?<![^\s+(])pg_query",
        "(?<![^\s+(])pg_send_query",

        # SQLite SQL Injection
        "(?<![^\s+(])sqlite_array_query",
        "(?<![^\s+(])sqlite_exec",
        "(?<![^\s+(])sqlite_query",
        "(?<![^\s+(])sqlite_single_query",
        "(?<![^\s+(])sqlite_unbuffered_query",

        # PDO SQL Injection
        "->arrayQuery",
        "->query",
        "->queryExec",
        "->singleQuery",
        "->querySingle",
        "->exec",
        "->execute",
        "->unbufferedQuery",
        "->real_query",
        "->multi_query",
        "->send_query",

        # WordPress SQL Injection
        "wpdb->query",
        "wpdb->get_var",
        "wpdb->get_row",
        "wpdb->get_col",
        "wpdb->get_results",
        "wpdb->replace",
    ]

    blacklist = [
        "mysql_real_escape_string",
        "pg_escape_string",
        "sqlite_escape_string",
        "wpdb->prepare",
        "intval",
        "esc_sql"
    ]
