from flask import Blueprint, render_template_string
from db import get_db_connection 

# app = Flask(__name__)
fetch_all_app = Blueprint('fetch_all', __name__)

@fetch_all_app.route('/fetch_all', methods=['GET'])
def fetch_all():
    try:
        # Fetch all visitors from the database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM visitors")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        return f"An error occurred: {e}"

    # Render the visitors in an HTML table
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>All Visitors</title>
    </head>
    <body>
        <h1>All Visitors</h1>
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Mobile</th>
                <th>Email</th>
                <th>Contact Person</th>
                <th>Visit Reason</th>
                <th>Timestamp</th>
            </tr>
            {% for row in rows %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
                <td>{{ row[4] }}</td>
                <td>{{ row[5] }}</td>
            </tr>
            {% endfor %}
        </table>
        <br>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """, rows=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
