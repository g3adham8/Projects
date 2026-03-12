import sqlite3
db = sqlite3.connect("app.db")
cr = db.cursor()
uid = "1"
cr.execute(
    f"create table if not exists skills (id integer primary key , skill_name text , skill_progress text , user_id integer) ")


def save_close():
    db.commit()
    db.close()
    print("database is closed")


input_message = """
What Do You Want To Do?
"s" => show all skills
"a" => add a new skill
"u" => update a skill progress 
"d" => delete skill
"q" => quit the app
You choose: """
user = input(input_message).strip().lower()
command_list = ["s", "a", "u", "d", "q"]


def show_skills():
    cr.execute(f"select * from skills where user_id = '{uid}'")
    result = cr.fetchall()
    print(f"you have {len(result)} skills")
    if len(result) > 0:

        print("showing skill in progress ")
    for row in result:
        print(f"your skill ==> {row[1]}")
        print(f"progress ==> {row[2]}%")
    save_close()


def add_skills():
    sn = input("Enter your skill name : ").strip().capitalize()
    prog = input("write skill progress: ").strip()
    cr.execute(
        f"insert into skills (skill_name , skill_progress , user_id) values ('{sn}' , '{prog}' , '{uid}') ")
    save_close()


def update_skills():
    sn = input("Enter your skill name : ").strip().capitalize()
    new_prog = input("write a new skill progress: ").strip()
    cr.execute(
        f"update skills set skill_progress = '{new_prog}' where skill_name = '{sn}' and user_id = '{uid}'")
    save_close()


def delete_skills():
    sn = input("Enter your skill name : ").strip().capitalize()
    cr.execute(
        f"delete from skills where skill_name = '{sn}' and user_id = '{uid}' ")

    save_close()


if user in command_list:
    # print(f"command found {user}")
    if user == 's':
        show_skills()
    elif user == 'a':
        add_skills()
    elif user == 'u':
        update_skills()
    elif user == 'd':
        delete_skills()
    else:
        print("app is closed")
        save_close()
else:
    print("Invalid letter ")
