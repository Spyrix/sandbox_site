#This is the main file for my budget app!
import logging
import sys
import sqlite3
import random

'''
#main#
Function containing the main loop of the program.

'''
def main():
    #Console input - if there are no arguments, then we're use commandline
    if(len(sys.argv)==1):
        command_line_loop()
    #else, run the functions individually, based on arguments

def command_line_loop():
    print('Hello! Please tell me your username to view your budget. This is debug.')

    if(doesUserExist(input())):
        print('Logging in...')
    else:
        print('User does not exist, would you like to create one? Y/N')
        UserCreateCon = True;
        while(UserCreateCon):
            choice = input()
            if(choice=='Y'):
                print('Creating User... what would you like their name to be?')
                temp_user = input()
                query_create_user(temp_user)
                print('Created user -- '+temp_user)
            elif(choice=='N'):
                print('Okay... leaving program!')
                sys.exit()
            else:
                print('Please try that again!')

#Initialize the connection for all the queries and the sets
def init_connection():
    conn = sqlite3.connect('budget.db')
    cur = conn.cursor()
    return (cur,conn)

#GET functions
def query_current_budget(user):
    cur = init_connection()
    return cur.execute("SELECT * FROM budget WHERE budgetID = (SELECT budgetID FROM users where name = ?)", user)

def query_transaction_history(user):
    cur = init_connection()
    return cur.execute("SELECT * FROM transactions WHERE budgetID = (SELECT budgetID FROM users where name = ?)", user)

def query_create_user(user):
    cur,conn = init_connection()
    #generate random 10 digit number for budgetID, make sure it's not already in use
    temp_create_budget_id = True
    temp_budgetID = 0
    while(temp_createBudget_id):
        temp_budget_id = round(random.randint(0,10000000000))
        c = cur.execute("SELECT * FROM users WHERE budgetID = ?",(temp_budget_id,))
        if(len(c.fetchall())==0):s
            temp_create_budget_id = False
    cur.execute("INSERT INTO users (name,budgetID,monthlyIncome) VALUES(?,?,0)", (user,temp_budget_id,))
    conn.commit()
    conn.close()

def does_user_exist(user):
    cur,conn = init_connection()
    exist = False
    c = cur.execute("SELECT * FROM users where name = ?", (user,))
    if(len(c.fetchall())>0):
        exist = True
    conn.close()
    return exist

#SET Functions
def update_user_monthly_income(user,income):
    cur,conn = init_connection()
    cur.execute("UPDATE users SET monthlyIncome=? WHERE name = ?", (income,user,))
    conn.commit()
    conn.close()

def insert_transaction(user,category,description,amount):
    cur,conn = init_connection()
    #generate random 10 digit number for budgetID, make sure it's not already in use
    temp_create_tran_id = True
    temp_tranID = 0
    while(temp_createtran_id):
        temp_tran_id = round(random.randint(0,10000000000))
        c = cur.execute("SELECT * FROM transactions WHERE transactionID = ?",(temp_tran_id,))
        if(len(c.fetchall())==0):s
            temp_create_tran_id = False
    cur.execute("INSERT INTO transactions (category,amount,description,budgetID,transactionID) VALUES(?,?,?,?)", (category,amount,description,user,temp_tranID))
    conn.commit()
    conn.close()

def update_transaction(user,transaction):
    cur,conn = init_connection()
    cur.execute("SELECT * FROM transactions WHERE user = ?", (user,))
    conn.commit()
    conn.close()

def select_transaction_categories(user):
    cur,conn = init_connection()
    c = cur.execute("SELECT * FROM transactions WHERE user = ?", (user,))
    conn.commit()
    conn.close()
    return c;

def delete_transaction(user,transaction):

#def delete_user(user):



#Run main
main()
