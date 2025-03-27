from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect('db/blogs.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, team_leader, job_description, work_size_hours,
               collaborators_ids, start_date, end_date, is_finished 
        FROM Jobs
    ''')
    jobs = cursor.fetchall()

    conn.close()

    return render_template_string(
        '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Jobs Table</title>
            <style>
                table {
                    font-family: Arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }
        
                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
        
                tr:nth-child(even) {
                    background-color: #eeeeee;
                }
            </style>
        </head>
        <body>
            <h1>Таблица задач</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Руководитель</th>
                        <th>Описание</th>
                        <th>Размер работы (часов)</th>
                        <th>Коллабораторы</th>
                        <th>Дата начала</th>
                        <th>Дата окончания</th>
                        <th>Завершено?</th>
                    </tr>
                </thead>
                <tbody>
                    {% for job in jobs %}
                    <tr>
                        <td>{{ job[0] }}</td>
                        <td>{{ job[1] }}</td>
                        <td>{{ job[2] }}</td>
                        <td>{{ job[3] }}</td>
                        <td>{{ job[4] }}</td>
                        <td>{{ job[5] }}</td>
                        <td>{{ job[6] }}</td>
                        <td>{{ 'Да' if job[7] == 1 else 'Нет' }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </body>
        </html>
        ''',
        jobs=jobs
    )


if __name__ == '__main__':
    app.run(debug=True)