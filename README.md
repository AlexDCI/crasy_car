# crasy_car
# Django Project Setup Guide

## Requirements
- Python 3.11+
- PostgreSQL 13+
- pip

---

# Car Sales Platform

This is a web-based platform designed for posting and searching car sales advertisements. The platform provides a user-friendly interface with multi-level authorization and role-based functionality.

---

## Features

### Multi-Level Authorization
- **Manager**: Oversees the platform, manages user accounts, and ensures compliance with the platform's policies.
- **Seller**: Can create and manage advertisements for cars they wish to sell.
- **Buyer**: Can search for cars using various filters and parameters.

### Core Functionality
1. **Sellers**:
   - Post advertisements with details such as make, model, year, price, and more.
   - Manage their listings (edit or delete ads).
2. **Buyers**:
   - Search for cars using filters like price range, brand, year, location, and other parameters.
   - View detailed car information and contact sellers.
3. **Managers**:
   - Manage platform users and monitor advertisements for quality and policy adherence.

### Frontend
- Built with **Bootstrap**, providing a responsive and clean user interface for both desktop and mobile devices.

### Backend
- Managed with **Django**, ensuring scalability and robust functionality.

### Database
- Utilizes **PostgreSQL** for reliable and efficient database management.
- Stores user information, car advertisements, and transaction history.

---

## Technology Stack

- **Programming Language**: Python (Django Framework)
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap)
- **Database**: PostgreSQL
- **Authentication**: Django's built-in authentication system with multi-role support
- **Deployment**: Configured to run on local or cloud servers

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <project_directory>
