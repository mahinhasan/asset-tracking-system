# Corporate Asset Tracking System

The Corporate Asset Tracking System is a web application built with Django that allows companies to efficiently track and manage their corporate assets, including phones, tablets, laptops, and other equipment assigned to employees.

## Features

### Companies Management
- **Add, Edit, and Delete Companies**: Easily manage company information, including name, industry, and founding date.
- **View Company Details**: Access detailed information about each company, including employees and assigned devices.

### Employees Management
- **Add, Edit, and Delete Employees**: Maintain employee records with details such as name, position, and contact information.
- **Assign Devices to Employees**: Assign devices to employees for specific periods, with tracking of checkout and return dates.
- **View Employee Devices**: See a list of devices assigned to each employee and their checkout history.

### Devices Management
- **Add, Edit, and Delete Devices**: Manage device inventory, including details like device type, model, and serial number.
- **Track Device Checkout History**: Keep track of when devices were checked out and returned, along with the condition of the device at each event.
- **Log Device Condition**: Log the condition of devices when they are checked out and returned to ensure accountability and maintenance.

### Authentication and Authorization
- **User Authentication**: Secure access to the application with user authentication.
- **Role-Based Access Control**: Control access to certain features based on user roles, ensuring data security and privacy.

### API
- **RESTful API**: Expose API endpoints for accessing company, employee, and device data.
- **Django REST Framework**: Utilize Django REST Framework for building the API, providing powerful tools for serialization, authentication, and more.

## Installation and Setup

### Requirements
- Python 3.x
- Django
- Django REST Framework


