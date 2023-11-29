

# Django Quotes Website

## Overview
This project is a Django-based web application that emulates the functionality of http://quotes.toscrape.com. It includes features for user registration and login, adding new authors and quotes by registered users, and viewing quotes and authors. The project also involves migrating existing data from MongoDB to PostgreSQL.

## Features
- **User Authentication**:
  - Registration and login functionality for users.
- **Author and Quote Management**:
  - Registered users can add new authors and quotes.
- **Database Migration**:
  - Migration of data from MongoDB to PostgreSQL (optional).
- **Public Access**:
  - Publicly accessible pages for viewing authors and quotes.
- **Pagination**:
  - Implementation of 'next' and 'previous' buttons for quote navigation.

## Implementation Details
- **Django Framework**:
  - Used for building the web application.
- **User Authentication**:
  - Django's built-in authentication system for handling user accounts.
- **Author and Quote Models**:
  - Django models for representing authors and quotes.
- **Database Migration**:
  - Custom script for migrating data from MongoDB to PostgreSQL.
- **Views and Templates**:
  - Django views and templates for displaying authors and quotes, including pagination.

## Usage
1. **User Registration and Login**:
   - Users can register and log in to add authors and quotes.
2. **Adding Authors and Quotes**:
   - Registered users can add new authors and quotes through the website interface.
3. **Viewing Authors and Quotes**:
   - All users can view the list of authors and quotes.
   - Pagination is implemented for easier navigation.

## Installation and Dependencies
- Clone the repository.
- Requires Python, Django, MongoDB, and PostgreSQL.
- Optional: MongoDB client libraries for Django if continuing to use MongoDB for some data.
