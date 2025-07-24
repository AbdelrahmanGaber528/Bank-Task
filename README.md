# 🏦 Bank-Task

A simple Python console-based banking system using OOP, file handling, and exception management.

## 📁 Structure

Bank-Task/
├── oop 
    -- model
      --- Account.py
      --- Bank.py
    -- service
      --- AccountMethods.py
      --- BankOperations
    --main.py
├── precedural
    -- main.py
├── utils
    -- Exceptions.py 
    -- HandleInputs.py
    -- file_manager.py
    -- accounts-data.txt
├── README.md

Bank-Task/
├── oop/
│ ├── model/
│ │ ├── Account.py # Account class with balance, deposit, withdraw
│ │ └── Bank.py # Bank class managing multiple accounts
│ ├── service/
│ │ ├── AccountMethods.py # Operations on a single account
│ │ └── BankOperations.py # High-level bank functions
│ └── main.py # Main entry point for OOP-based version
│
├── procedural/
│ └── main.py # Procedural version of the same system
│
├── utils/
│ ├── Exceptions.py # Custom exceptions (e.g., InvalidAmount, AccountNotFound)
│ ├── HandleInputs.py # Validated input functions
│ ├── file_manager.py # Load/save accounts from file
│ └── accounts-data.txt # Persistent storage for accounts
│
└── README.md # You're here!
