import azure.functions as func
import datetime
import logging

app = func.FunctionApp()

@app.route(route="sqlInsert")
@app.sql_output(
    arg_name="outputTable",
    command_text="dbo.Users",
    connection_string_setting="SqlConnectionString"
)
def sqlInsertFn(req: func.HttpRequest, outputTable: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('SQL insert function triggered.')

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get("name")
        except ValueError:
            name = None

    if name:
        row = func.SqlRow({
            "Name": name,
            "CreatedAt": str(datetime.datetime.utcnow())
        })
        outputTable.set(row)
        return func.HttpResponse(f"Inserted {name} into SQL table.")
    else:
        return func.HttpResponse(
            "Please pass a name in the query string or body.",
            status_code=400
        )
