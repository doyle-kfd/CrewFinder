# CrewFinder

**CrewFinder** is a fictitious platform designed to connect captains and crew members in the sailing community. Whether you're a captain searching for crew to join your voyage or a sailor looking for exciting opportunities on the water, CrewFinder helps bring people together. With its simple and intuitive design, the platform makes it easy to create or apply for sailing trips.

This project was developed as part of a portfolio to showcase full-stack development skills. While it’s not a real application, CrewFinder demonstrates how captains and crew members could collaborate effortlessly through features like trip listings, applications, and profile management. Explore the possibilities of what such a platform could achieve!

The live link can be found here - [CrewFinder](https://crew-finder-410f29f97c51.herokuapp.com/)


# Table of contents

- [Crewfinder](#crewfinder)
  - [Table Of Contents](#table-of-contents)
  - [The Approach I Took](#the-approach-i-took)
  - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Imagery](#imagery)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
  - [User Stories](#user-stories)
  - [Data Model](#data-model)
  - [Testing](#testing)
  - [Security Features](#security-features)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
  - [Features](#features)
    - [Feature 1](#feature-1)
    - [Feature 2](#feature-2)
    - [Feature 3](#feature-3)
  - [Deployment On Heroku](#deployment-on-heroku)
  - [Forking The Repository](#forking-the-repository)
  - [Cloning The Repository](#cloning-the-repository)
  - [Languages](#languages)
  - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

# The Approach I Took

<details>

 <summary>Welcome</summary>

![PP4 Welcome](docs/readme_images/PP4%20Intro.png)
</details>

<details>

 <summary>Agenda</summary>

![PP4 Agenda](docs/readme_images/PP4%20Agenda.png)
</details>
<details>

 <summary>Introduction</summary>

![PP4 Intro](docs/readme_images/PP4%20General%20Introduction.png)
</details>
<details>

 <summary>The Problem</summary>

![PP4 The Problem](docs/readme_images/PP4%20The%20Proiblem%20I%20Solve.png )
</details>
<details>

 <summary>Target Audience</summary>

![PP4 Target Audience](docs/readme_images/PP4%20The%20Proiblem%20I%20Solve.png )
</details>
<details>

 <summary>Persona 1 - Captain</summary>

![PP4 Persona 1 - Captain](docs/readme_images/PP4%20Persona%201%20-%20Captain.png )
</details>
<details>

 <summary>Persona 2 - Crew</summary>

![PP4 Persona 1 - Captain](docs/readme_images/PP4%20Persona%202%20-%20Crew.png )
</details>
<details>

 <summary>Persona 2 - Crew</summary>

![PP4 Persona 1 - Captain](docs/readme_images/PP4%20Persona%202%20-%20Crew.png )
</details>
<details>

 <summary>Proposed Solution</summary>

![PP4 Proposed Solution](docs/readme_images/PP4%20Proposed%20Sulution.png )
</details>
<details>

 <summary>I Will Deliver</summary>

![PP4 I Will Deliver](docs/readme_images/PP4%20What%20I%20Will%20Deliver.png)
</details>
<details>

 <summary>Process Flow</summary>

![PP4 Process Flow](docs/readme_images/PP4%20Process%20Flow.png)
</details>
<details>

 <summary>README</summary>

![PP4 README](docs/readme_images/PP4%20README.png)
</details>
<details>

 <summary>Testing</summary>

![PP4 TESTING](docs/readme_images/PP4%20Testing.png)
</details>

# Design
The design of the site is clean and simple. It features colours and imagery supporting the marine theme.
The imagery reflects the target audience and the experience of crew and captains on trips.

### Color Scheme
![Colour Palette](docs/readme_images/Color%20Pallet.png)

The colours were picked to reflect and complement the marine nature of the site theme.

### Imagery
The images selected for the site theme are used to reflect the target audience. The are meant to create an excitement about the sailing experince.

### Fonts
Robot has been chosed as the primary font with sans-serif as the backup should the primary not load correctly.


### Wireframes

<details>

 <summary>Home Page</summary>

![Home Page](docs/wireframes/Home%20Page.png)
</details>
<details>

 <summary>About Us</summary>

![About Us](docs/wireframes/About%20Us.png)
</details>
<details>

 <summary>Contact Us</summary>

![Contact Us](docs/wireframes/Contact%20Us.png)
</details>

<details>

 <summary>Login</summary>

![Login](docs/wireframes/Login%20Page.png)
</details>

<details>

 <summary>Signup</summary>

![Signup](docs/wireframes/Signup%20Page.png)
</details>

<details>

 <summary>Admin Dashboard</summary>

![Admin Dashboard](docs/wireframes/Administrator%20Dashboard.png)
</details>

<details>

 <summary>Captains Dashboard</summary>

![Captains Dashboard](docs/wireframes/Captains%20Dashboard.png)
</details>

<details>

 <summary>Crew Dashboard</summary>

![Crew Dashboard](docs/wireframes/Crew%20Dashboard.png)
</details>

<details>

 <summary>Update Profile Form</summary>

![Update Profile Form](docs/wireframes/Update%20Profile%20Form.png)
</details>
<details>

 <summary>Complete Profile Form</summary>

![Complete Profile Form](docs/wireframes/complete%20profile%20form.png)
</details>


## Agile Methodology
I used Github to manage the development process using an agile approach.

I used two views, Kanban and a table to view progress.

[Kanban](https://github.com/users/doyle-kfd/projects/2/views/1)

[Table View](https://github.com/users/doyle-kfd/projects/2/views/2)

### User Stories

#### EPIC | User Registration, Approval And Authentication
- As a user, I want to register for an account with the option to select my role as either a captain or a crew member so that I can specify my participation in trips.

  - AC-1 The registration form includes fields for username, email, password, and role selection.
  - AC-2 Role selection is limited to "Captain" or "Crew."
  - AC-3 After successful registration, the user sees a message indicating that their account is pending admin approval.

- As an admin, I want to review new account registrations and approve or disapprove them so that only validated users can access the platform.

  - AC-1 Admin dashboard lists all pending accounts.
  - AC-2 Approved users are notified and gain access to the platform to complete their profile; disapproved users receive a notification.

- As an approved user, I want to complete my profile by adding information about my experience level and a bio, so that others can understand my skills and background.

  - AC-1 After admin approval, the user gains access to the profile setup page.
  - AC-2 The profile form includes fields for experience level and a bio.
  - AC-3 Form is styled using Crispy Forms and Bootstrap.
  - AC-4 Data saves successfully to the profile, and changes are visible on the dashboard.

- As an approved user, I want to view my profile on my dashboard, so I can see the information I’ve shared and make updates as needed.

  - AC-1 Dashboard displays user profile with fields for bio and experience level.
  - AC-2 The Edit option is available to update profile details.
  - AC-3 Changes save and update immediately upon submission.

- As a returning user, I want to log in and log out of my account securely to access my profile and trip features.

  - AC-1 The login form includes fields for email/username and password, with clear labels for each.
  - AC-2 Upon successful login with valid credentials, the user is redirected to their dashboard.
  - AC-3 A Logout link is available in the navigation bar when the user is logged in.
  - AC-4 Upon logging out, the user is redirected to the homepage.
  - AC-5 If a logged-out user tries to access a restricted page (e.g., dashboard or profile), they are redirected to the login page.


#### EPIC | Trip Management

- As a captain, I want to create a sailing trip with details like title, location, date, and the number of crew needed, so I can recruit crew members for specific journeys.

  - AC-1 The trip creation form is only accessible to users with the "Captain" role.
  - AC-2 Form includes fields for title, location, date, and crew needed.
  - AC-3 Created trip appears on the captain’s dashboard under "My Trips."

- As a captain, I want to view a list of my created trips, so I can manage my upcoming trips and review participant status.

  - AC-1 Dashboard lists all trips created by the captain, sorted by date.

- As a captain, I want to view detailed information about each trip I create, including a list of crew members who have joined, so I can manage and organize my crew effectively.

  - AC-1 The Trip Details page displays trip information and a list of confirmed crew members.
  - AC-2 Option to approve or reject crew requests (if applicable).

#### EPIC | Joining Trips

- As a crew member, I want to view a list of available sailing trips, so I can decide which ones I’d like to join.

  - AC-1 Page that displays a list of trips with open crew positions.
  - AC-2 Each trip entry includes title, location, date, and an option to request to join.

- As a crew member, I want to request to join a specific sailing trip, so I can participate and gain more experience.

  - AC-1 The join request option is available for crew members on the trip details page.
  - AC-2 Request updates the trip’s participant list as "Pending."
  - AC-3 Confirmation of successful join request appears on-screen.

- As a crew member, I want to view the trips I’ve joined on my dashboard, so I can keep track of my participation.

  - AC-1 Dashboard includes a "My Trips" section listing trips the user has joined.
  - AC-2 Trip status (e.g., Pending, Confirmed) displays for each entry.

- As a user, I want my experience to be tailored based on my role (captain or crew), so I only see actions and views relevant to my role.

  - AC-1 Captains have access to trip creation, management, and crew approval features.
  - AC-2 Crew members have access to trip browsing and join request features.
  - AC-3 Unauthorized users are redirected if attempting restricted actions.

#### EPIC | Role Based Access Control

- As an admin, I want to manage user roles effectively, so I can control access to specific features.

  - AC-1 The admin panel includes options to view and modify user roles.
  - AC-2 Role changes are saved and take immediate effect on user permissions.

- As a user, I want my experience to be tailored based on my role (captain or crew), so I only see actions and views relevant to my role.

  - AC-1 Captains have access to trip creation, management, and crew approval features.
  - AC-2 Crew members have access to trip browsing and join request features.
  - AC-3 Unauthorized users are redirected if attempting restricted actions.

#### EPIC | Platform UI And Testing

- As a user, I want rich-text capabilities in my profile bio, so I can add more detailed information about myself.

  - AC-1 Bio field on the profile form supports rich-text formatting via Summernote.
  - AC-2 Bio content displays properly in the profile view on the dashboard.

- As a user, I want the platform to have a clean and intuitive layout with easy navigation, so I can find features and complete actions quickly.

  - AC-1 Consistent styling across pages using Bootstrap and Crispy Forms.
  - AC-2 Navigation bar with links to key sections (dashboard, profile, trips).
  - AC-3 All pages are mobile-friendly and responsive.

#### EPIC | Static Pages

- As a visitor, I want an "About Us" page that describes the purpose of CrewFinder and the benefits of joining, so I can learn more about the platform.

  - AC-1 About Us page includes information on CrewFinder’s mission, team, and features.
  - AC-2 Page is accessible from the navigation bar for all users.

- As a visitor, I want to see a welcoming home page that provides an overview of the CrewFinder platform, so I can understand the purpose and features of the app.

  - AC-1 Home page includes a brief description of CrewFinder, a call-to-action to join, and links to key pages (About Us, Sailing Opportunities, Contact Us).
  - AC-2 Accessible from the navigation bar and visible to all users, including non-logged-in visitors.

- As a visitor, I want a "Contact Us" page where I can find information on how to reach CrewFinder’s team, so I can ask questions or get support.

  - AC-1 Contact Us page includes a contact form with fields for name, email, and message, along with any relevant contact details.
  - AC-2 Submitting the form sends a message to the CrewFinder team and displays a confirmation to the user.

#### EPIC | Dynamic Pages

- As a visitor, I want to see a welcoming home page that provides an overview of the CrewFinder platform and displays the three latest trips, so I can see current opportunities and understand the purpose of the app.

  - AC-1 Home page includes a description of CrewFinder and links to key pages (About Us, Sailing Opportunities, Contact Us).
  - AC-2 The three latest trips are displayed dynamically, showing title, location, date, and a link to the trip details.
  - AC-3 Accessible from the navigation bar and visible to all users, including non-logged-in visitors.

- As a visitor, I want to view a "Sailing Opportunities" page with a list of all available trips, so I can browse sailing options before signing up.

  - AC-1 Sailing Opportunities page lists all active trips, showing titles, locations, dates, and number of crew needed.

- As a visitor, I want a login page where I can enter my credentials to access the platform, so I can reach my account and profile.

  - AC-1 Login page includes fields for email/username and password, along with a “Forgot Password?” option.
  - AC-2 Successful login redirects to the user dashboard.

#### EPIC | Deployment And Testing

- As a developer, I want to deploy the app to Heroku frequently, so I can verify that each feature works as expected in a production-like environment.

  - AC-1 Initial deployment to Heroku occurs on Day 1.
  - AC-2 Subsequent features are deployed to Heroku and verified after implementation.

- As a developer, I want to configure Whitenoise for static file handling, so I can manage CSS and JavaScript assets effectively in production.

  - AC-1 Whitenoise is installed and configured to handle static files on Heroku.
  - AC-2 Static assets load correctly and are accessible in the production environment.

- As a developer, I want to write unit tests for critical models and views, so I can ensure the app behaves as expected.

  - AC-1 Key models (e.g., Account, SailingTrip, CrewBooking) have associated unit tests.
  - AC-2 Critical views (e.g., registration, trip creation) are tested for expected behaviour.


## Data Model

I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.

Django AllAuth was used for the user authentication system.

#### Defined Relationships


**User to Trip:**
A User can be a Captain for multiple Trips.

User.id to Trip.captain_id with a 1 to many relationship.

**Trip to CrewBooking:**
A Trip can have multiple CrewBooking records.

Trip.id to CrewBooking.trip_id with a 1 to many relationship.

**User to CrewBooking:**
A User (Crew) can apply to multiple Trips via CrewBooking.

User.id to CrewBooking.user_id with a 1 to many relationship.

#### The CrewFinder ERD Model:

![CrewFinder Database Schema](docs/readme_images/CrewFinder%20ERD.png)

## Testing

#### Testing And Results Can Be Found [here](/TESTING.md)


# My Apps

### Accounts App Detail

<details>

<summary>Views File </summary>

# `accounts/views.py`


This Accounts application handles various user management operations, including profile completion, dashboards for different roles, and custom authentication workflows such as signup, login, and logout.

---

### Features

#### 1. **User Profile Completion**
- **Function**: `complete_profile(request)`
  - Allows users to complete their profile if it hasn't been completed yet.
  - Redirects users to the dashboard if their profile is already complete.
  - Displays a form for adding additional details such as bio, experience, and profile photo.

---

#### 2. **User Dashboards**
- **Function**: `dashboard(request)`
  - Displays different dashboards based on the user's role:
    - **Administrators**: Redirected to the `admin_dashboard`.
    - **Captains**: Shows trips created by the captain, along with crew applications.
    - **Crew Members**: Displays the trips they have applied for.

---

#### 3. **Registration Pending View**
- **Function**: `registration_pending(request)`
  - Displays a page for users awaiting admin approval after signup.

---

#### 4. **Custom Authentication Views**
- **Custom Login**: `CustomLoginView`
  - Redirects users to specific pages based on their role and profile status:
    - Admins: Redirected to the admin dashboard.
    - Users with incomplete profiles: Redirected to the profile completion page.
  - Includes handling for the `next` parameter for redirecting users post-login.
  
- **Custom Signup**: `CustomSignupView`
  - Redirects newly registered users to the `registration_pending` page.

---

#### 5. **Admin Dashboard**
- **Function**: `admin_dashboard(request)`
  - Allows administrators to view a list of captains and crew members.
  - Excludes superusers from the list for security purposes.

---

#### 6. **Custom Logout**
- **Custom Logout**: `CustomLogoutView`
  - Displays a success message upon logout and redirects users to the home page.

---

#### 7. **Profile Update**
- **Function**: `update_profile(request)`
  - Allows users to update their profile details and upload files (e.g., profile photo).

---

#### 8. **Crew Member Profiles**
- **Function**: `crew_profile(request, user_id, trip_id)`
  - Allows captains to view and manage the profiles of crew members who applied for their trips.
  - Captains can update the status of crew applications using the `CrewBookingStatusForm`.

---

#### 9. **Edit User**
- **Function**: `edit_user(request, user_id)`
  - Allows administrators to edit user details such as roles and approval statuses.
  - Prevents editing of superusers and other administrator accounts.

---

#### 10. **Forms**
- **`CrewBookingStatusForm`**:
  - Form to update the status of crew applications (e.g., "confirmed," "pending").

---

### Workflow

1. A user signs up and is redirected to the `registration_pending` page.
2. An administrator reviews and approves the user.
3. Once approved, the user receives a notification and can log in to complete their profile.
4. Captains create trips and manage applications from crew members.
5. Crew members apply for trips and track their application statuses.

---

### Security Measures

- **Access Control**:
  - The `login_required` decorator ensures that only authenticated users can access protected views.
  
- **Role-Based Permissions**:
  - Administrators cannot edit or delete superusers.
  - Different dashboards are displayed based on user roles (e.g., captain, crew).

- **Optimized Queries**:
  - Uses `prefetch_related` and `select_related` to minimize database queries when fetching related data.

---

### Key Technologies
- **Role-Based Access**:
  - Captains and crew members have different interfaces.
  - Administrators have advanced controls for managing users.

- **Approval Workflow**:
  - New users must await admin approval before gaining full access to the system.

- **Custom Authentication**:
  - Overrides Django Allauth's login and signup workflows to enforce custom logic.

- **Efficient Database Queries**:
  - Optimized using Django ORM features like `prefetch_related` and `select_related`.

---

This system efficiently manages users, enforces role-specific functionality, and implements a robust approval-based workflow.

</details>

<details>

<summary> URLS File </summary>

# `accounts/urls.py`

## URL Configuration Overview

This section describes the URL routing defined in the `urls.py` file. It maps specific URL patterns to corresponding views and includes additional routes from third-party apps, such as Django Allauth.

---

### **Imports**

- **Core Django Imports**:
  - `path`: Used to define URL patterns.
  - `include`: Allows inclusion of URL configurations from other apps.
  - `static`: Enables serving of static and media files in development.
  - `settings`: Provides access to project-level settings like `MEDIA_URL`.

- **Local Imports**:
  - `views`: Imports all views defined in the `views.py` file.
  - Specific class-based and function-based views (e.g., `CustomSignupView`, `dashboard`) are imported for use in the `urlpatterns` list.

---

### **URL Patterns**

The `urlpatterns` list defines the routing for various user operations, such as authentication, profile management, and admin-specific tasks. 

#### **1. Authentication and Account Management**
- **`signup/`**:
  - View: `CustomSignupView`
  - Name: `account_signup`
  - Handles user signup and redirects users to the registration pending page.

- **`login/`**:
  - View: `CustomLoginView`
  - Name: `account_login`
  - Handles user login and redirects users based on role and profile completion.

- **`logout/`**:
  - View: `CustomLogoutView`
  - Name: `account_logout`
  - Logs users out and redirects them to the home page with a success message.

---

#### **2. Profile-Related URLs**
- **`complete_profile/`**:
  - View: `complete_profile`
  - Name: `complete_profile`
  - Allows users to complete their profile after registration approval.

- **`registration_pending/`**:
  - View: `registration_pending`
  - Name: `registration_pending`
  - Displays a pending approval page for newly registered users awaiting admin approval.

- **`dashboard/`**:
  - View: `dashboard`
  - Name: `dashboard`
  - Displays a role-specific dashboard for captains, crew, or administrators.

- **`admin_dashboard/`**:
  - View: `admin_dashboard`
  - Name: `admin_dashboard`
  - Displays a management dashboard for administrators to manage users.

- **`update_profile/`**:
  - View: `update_profile`
  - Name: `update_profile`
  - Allows users to update their profile details and upload photos.

---

#### **3. Crew Profile and User Management**
- **`profile/<int:user_id>/<int:trip_id>/`**:
  - View: `crew_profile`
  - Name: `crew_profile`
  - Displays and manages the profile of a crew member for a specific trip.

- **`edit_user/<int:user_id>/`**:
  - View: `edit_user`
  - Name: `edit_user`
  - Allows administrators to edit user details, such as roles and approval status.

---

#### **4. Third-Party Integration**
- **`''`**:
  - Includes all routes from Django Allauth for handling additional authentication features (e.g., password reset, email verification).

---

#### **5. Static and Media Files**
- **Static Media Serving**:
  - `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`:
    - Ensures that media files (e.g., user-uploaded profile photos) are served correctly during development.

---

### **Routing Behavior**

1. **Authentication and Role-Based Redirects**:
   - Users are routed based on their role (e.g., admin, captain, crew) and approval status (e.g., pending approval, profile completion).

2. **Dynamic Routing**:
   - The `profile/<int:user_id>/<int:trip_id>/` route dynamically uses parameters to display and manage specific crew applications for trips.

3. **Flexible Account Management**:
   - Administrators have dedicated routes like `edit_user/` for managing user accounts.

4. **Third-Party Integration**:
   - The use of `include('allauth.urls')` ensures seamless integration with Django Allauth's authentication workflows.

---

</details>

<details>

<summary>Signals File</summary>

# `accounts/signals.py`

## Signals Overview

The `signals.py` file contains logic to respond to changes in the database triggered by specific events. This ensures dynamic updates, notifications, and status management across the system without manual intervention.

---

### **Key Signals**

#### **1. `notify_admin_of_new_user`**
- **Trigger**: `post_save` signal on the `User` model.
- **Purpose**: Sends an email notification to all administrators when a new user registers with a `PENDING` approval status.
- **Logic**:
  - Retrieves emails of users with the `ADMINISTRATOR` role.
  - Sends an email to notify administrators that a new user is awaiting approval.

---

#### **2. `notify_user_of_approval`**
- **Trigger**: `post_save` signal on the `User` model.
- **Purpose**: Activates a user account and sends an approval email when their registration is approved.
- **Logic**:
  - Sets the user's `is_active` field to `True` upon approval.
  - Sends an email with a link to complete their profile.

---

#### **3. `notify_user_of_disapproval`**
- **Trigger**: `post_save` signal on the `User` model.
- **Purpose**: Deactivates a user account and notifies the user via email if their registration is disapproved.
- **Logic**:
  - Sets the user's `is_active` field to `False` if disapproved.
  - Sends an email explaining the disapproval and suggests contacting support.

---

#### **4. `adjust_crew_needed`**
- **Trigger**: `post_save` signal on the `CrewBooking` model.
- **Purpose**: Adjusts the `crew_needed` field of a trip when the status of a crew booking changes.
- **Logic**:
  - If a booking is confirmed, decrements the `crew_needed` count for the associated trip.
  - If a confirmed booking status changes to another status, increments the `crew_needed` count.

---

#### **5. `increment_crew_needed_on_delete`**
- **Trigger**: `post_delete` signal on the `CrewBooking` model.
- **Purpose**: Increments the `crew_needed` field of a trip when a confirmed booking is deleted.
- **Logic**:
  - Ensures that the `crew_needed` count is incremented only for confirmed bookings.

---

### **Workflow of Signals**

1. **User Registration**:
   - When a user registers, the `notify_admin_of_new_user` signal triggers, notifying administrators of the pending approval.

2. **Approval or Disapproval**:
   - If approved, the `notify_user_of_approval` signal activates the user's account and sends an email.
   - If disapproved, the `notify_user_of_disapproval` signal deactivates the account and sends a notification.

3. **Crew Booking Status Changes**:
   - The `adjust_crew_needed` signal dynamically updates the `crew_needed` field for trips based on booking confirmations or status changes.

4. **Crew Booking Deletion**:
   - When a confirmed booking is deleted, the `increment_crew_needed_on_delete` signal ensures that the trip's `crew_needed` count is updated.

---

### **Key Features**

- **Dynamic Updates**:
  - Signals automatically handle changes to related fields (e.g., `crew_needed` for trips) without requiring explicit logic in the views or models.

- **Notifications**:
  - Sends emails to administrators and users based on registration and approval workflows.

- **Data Integrity**:
  - Prevents invalid values, such as negative `crew_needed` counts, through logical constraints.

- **Role-Based Behavior**:
  - Administrators are informed of pending registrations, while users are notified of their approval or disapproval status.

---

</details>

<details>
<summary>Models</summary>

# `accounts/models.py`

## Custom User Model

The `User` model extends Django's built-in `AbstractUser` to provide additional fields and functionality tailored to the application's requirements. This model supports role-based behavior, approval workflows, and sailing-related profile data.

---
# Custom User Model

The `User` model extends Django's built-in `AbstractUser` to provide additional fields and functionality tailored to the application's requirements. This model supports role-based behavior, approval workflows, and sailing-related profile data.

---

## Model Attributes

### **1. Role Choices**
Defines the roles a user can have:
- **`CAPTAIN`**: Represents a captain who can create trips and manage crew applications.
- **`CREW`**: Represents a crew member who can apply for trips.
- **`ADMINISTRATOR`**: Represents an administrator responsible for approving registrations and managing users.

```python
ROLE_CHOICES = [
    ('captain', 'Captain'),
    ('crew', 'Crew'),
    ('administrator', 'Administrator'),
]
```

### **2. Approval Status**

Tracks the user's registration status, ensuring a controlled workflow for activating or rejecting user accounts:

- **`PENDING`**: The default status for new registrations awaiting admin approval.
- **`APPROVED`**: Indicates the user has been approved by an administrator and their account is active.
- **`DISAPPROVED`**: Indicates the user's registration has been rejected, and their account is inactive.

```python
APPROVAL_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('disapproved', 'Disapproved'),
]
```

### **3. Sailing Experience**

Defines the sailing experience levels users can select, allowing them to specify their skill level and qualifications. Examples include:

- **`None`**: Default experience level.
- **`RYA Competent Crew`**
- **`RYA Dayskipper`**
- **`RYA Yachtmaster Coastal`**
- **`RYA Yachtmaster Offshore`**
- **`RYA Yachtmaster Ocean`**

```python
EXPERIENCE_CHOICES = [
    ('None', 'None'),
    ('RYA Competent Crew', 'RYA Competent Crew'),
    ('RYA Dayskipper', 'RYA Dayskipper'),
    ('RYA Yachtmaster Coastal', 'RYA Yachtmaster Coastal'),
    ('RYA Yachtmaster Offshore', 'RYA Yachtmaster Offshore'),
    ('RYA Yachtmaster Ocean', 'RYA Yachtmaster Ocean'),
]
```

### **4. Custom Fields**

The `User` model includes the following additional fields:

| Field Name         | Description                                                                                      | Default         |
|--------------------|--------------------------------------------------------------------------------------------------|-----------------|
| **`role`**         | The user's role (`Captain`, `Crew`, or `Administrator`).                                         | `crew`          |
| **`bio`**          | An optional biography field where users can provide personal details.                           | `None`          |
| **`experience_level`** | Legacy field for user sailing experience (optional).                                           | `None`          |
| **`approval_status`** | Tracks the user's approval status (`Pending`, `Approved`, or `Disapproved`).                    | `pending`       |
| **`profile_completed`** | A boolean indicating whether the user has completed their profile.                            | `False`         |
| **`is_active`**    | Indicates if the user's account is active (automatically updated based on `approval_status`).    | `False`         |
| **`experience`**   | Tracks the user's sailing experience level (e.g., `RYA Competent Crew`).                         | `None`          |
| **`photo`**        | Optional field for storing the user's profile photo using Cloudinary.                           | `None`          |

### **Methods**

#### **1. `save` Method**
The `save` method is overridden to automate updates to the `is_active` field based on the user's `approval_status`. 

- **Behavior**:
  - If the `approval_status` is **`APPROVED`**, the `is_active` field is set to `True`.
  - If the `approval_status` is **`PENDING`** or **`DISAPPROVED`**, the `is_active` field is set to `False`.

```python
def save(self, *args, **kwargs):
    if self.approval_status == self.APPROVED:
        self.is_active = True
    elif self.approval_status in [self.DISAPPROVED, self.PENDING]:
        self.is_active = False
    super().save(*args, **kwargs)
```
#### **2. `__str__` Method**
The `__str__` method returns the username as the string representation of the user. 

- **Purpose**:
  - Makes it easy to reference users in admin interfaces and logs.
  - Provides a clear and intuitive way to display user objects.

```python
def __str__(self):
    return self.username
```
### **Key Features**

#### **Role-Based Behavior**
- **Captains**:
  - Create trips and manage crew applications.
- **Crew Members**:
  - Apply for trips and track application status.
- **Administrators**:
  - Oversee user approvals and manage the system's functionality.

#### **Approval Workflow**
- Newly registered users default to **`PENDING`** status.
- Administrators:
  - Must approve users to activate their accounts (`is_active = True`).
  - Can disapprove users, resulting in deactivation (`is_active = False`).

#### **Sailing Profile Data**
- Captures:
  - Users' sailing experience levels.
  - Biographies.
  - Profile photos.

#### **Cloudinary Integration**
- Profile photos are uploaded and securely stored using **Cloudinary**.

---

### **Workflow**

#### **User Registration**
1. New users register and select a role (e.g., **Captain**, **Crew**).
2. Default `approval_status` is set to **`PENDING`**.

#### **Approval Process**
1. Administrators review registrations.
2. Actions:
   - **Approve**: Users are assigned **`APPROVED`** status, making their accounts active.
   - **Disapprove**: Users are assigned **`DISAPPROVED`** status, deactivating their accounts.

#### **Profile Completion**
1. Once approved, users are prompted to complete their profiles.
2. Users can provide additional details, such as:
   - Biography.
   - Sailing experience.
   - Profile photo.

</details>

<details>

<summary>Forms</summary>

# `accounts/forms.py`

## Forms

This module defines custom forms used in the application to handle user registration, profile completion, and administrative user management.

---

## **1. CustomSignupForm**

A custom signup form that extends `SignupForm` from `django-allauth`. It allows users to select their role during registration and sets initial user status.

### **Attributes**
- **`role`**: A dropdown field for selecting the user's role. Options are defined by `User.ROLE_CHOICES`.

### **Methods**
#### **`custom_signup(request, user)`**
Assigns the selected role to the user and sets their initial status.
- **Args**:
  - `request (HttpRequest)`: The HTTP request object.
  - `user (User)`: The user instance being created.
- **Returns**: 
  - `User`: The updated user instance.

## **2. ProfileCompletionForm**

A form that allows users to complete their profiles by providing additional details such as bio, sailing experience, and profile photo.

---

### **Meta Attributes**

- **`model`**: The `User` model associated with the form.
- **`fields`**: Fields included in the form:
  - `'username'`
  - `'email'`
  - `'bio'`
  - `'experience'`
  - `'photo'`
- **`help_texts`**: Removes the default help text for the `username` field.

---

### **Methods**

#### **`__init__(*args, **kwargs)`**
Initializes the form and sets the `username` and `email` fields as read-only.

#### **`save(commit=True)`**
Saves the form data to the user instance without modifying the user's password.

- **Args**:
  - `commit (bool)`: Whether to save the user instance immediately.
- **Returns**:
  - `User`: The updated user instance.

---

## **3. EditUserForm**

A form designed for administrators to edit user details, including their role, approval status, experience, and profile photo.

---

### **Meta Attributes**

- **`model`**: The `User` model associated with the form.
- **`fields`**: Fields included in the form:
  - `'username'`
  - `'email'`
  - `'role'`
  - `'approval_status'`
  - `'experience'`
  - `'photo'`

---

</details>

<details>

<summary>Apps</summary>

# `accounts/apps.py`

## `AccountsConfig`

The `AccountsConfig` class is a configuration class for the `accounts` application. It extends Django's `AppConfig` and ensures proper initialization and configuration of the app's settings and signals.

---

### **Attributes**

- **`default_auto_field`**:
  - Specifies the type of auto-generated field for primary keys.
  - Default: `'django.db.models.BigAutoField'`.

- **`name`**:
  - The name of the application.
  - Default: `'accounts'`.

---

### **Methods**

#### **`ready()`**
The `ready` method is called when the application starts. It imports and registers signal handlers, ensuring that the application's signals are active.

- **Purpose**:
  - To load the `accounts.signals` module and initialize signal handlers.
- **Key Behavior**:
  - Ensures signals are properly registered for handling custom user-related events.

---

</details>

<details>

<summary>Admin</summary>

# `accounts/admin.py`

This module customizes the Django admin interface for the `User` model, providing enhanced control over user management. The `CustomUserAdmin` class extends `UserAdmin` to include additional functionality and permissions tailored to the application's requirements.

---

## **CustomUserAdmin**

The `CustomUserAdmin` class customizes the admin interface for the `User` model, allowing administrators to manage users effectively with role-based restrictions and customized display fields.

---

### **Attributes**

- **`list_display`**:
  - Specifies the fields to display in the admin list view.
  - Example: `'username'`, `'email'`, `'approval_status'`, `'is_active'`, `'role'`, `'is_staff'`.

- **`list_filter`**:
  - Adds filtering options to the admin interface.
  - Example: `'approval_status'`, `'is_active'`, `'role'`.

- **`search_fields`**:
  - Enables search functionality in the admin interface.
  - Example: `'username'`, `'email'`.

- **`ordering`**:
  - Specifies the default ordering for the list view.
  - Example: `'date_joined'`.

- **`list_editable`**:
  - Specifies fields editable directly in the list view.
  - Example: `'approval_status'`.

- **`fieldsets`**:
  - Groups fields displayed on the user detail page into sections.

---

### **Methods**

#### **1. `get_fieldsets(request, obj=None)`**
Customizes the fields displayed in the admin detail view based on the role of the logged-in user.
- **Args**:
  - `request (HttpRequest)`: The current request object.
  - `obj (User)`: The user object being edited (optional).
- **Returns**:
  - `tuple`: The fieldsets to display in the admin interface.

---

#### **2. `get_queryset(request)`**
Filters the queryset to exclude superusers and limit visibility to captains and crew for administrators.
- **Args**:
  - `request (HttpRequest)`: The current request object.
- **Returns**:
  - `QuerySet`: The filtered queryset.

---

#### **3. `has_add_permission(request)`**
Restricts the ability to add new users to superusers only.
- **Args**:
  - `request (HttpRequest)`: The current request object.
- **Returns**:
  - `bool`: `True` if the user is a superuser, otherwise `False`.

---

#### **4. `has_change_permission(request, obj=None)`**
Prevents administrators from editing superuser or administrator accounts.
- **Args**:
  - `request (HttpRequest)`: The current request object.
  - `obj (User)`: The user object being edited (optional).
- **Returns**:
  - `bool`: `True` if the user has permission, otherwise `False`.

---

#### **5. `has_delete_permission(request, obj=None)`**
Prevents deletion of superuser accounts.
- **Args**:
  - `request (HttpRequest)`: The current request object.
  - `obj (User)`: The user object being deleted (optional).
- **Returns**:
  - `bool`: `True` if the user has permission, otherwise `False`.

---

#### **6. `save_model(request, obj, form, change)`**
Automatically updates the `is_active` field based on the user's `approval_status`.
- **Args**:
  - `request (HttpRequest)`: The current request object.
  - `obj (User)`: The user object being saved.
  - `form (ModelForm)`: The form instance with the submitted data.
  - `change (bool)`: `True` if the object is being updated, otherwise `False`.

---


</details>

<details>

<summary>Adapter</summary>

# `accounts/adapter.py`

## Custom Account Adapter

The `CustomAccountAdapter` class customizes Django Allauth's default behavior for account management. It modifies redirection logic and login behavior to align with the application's requirements, such as preventing auto-login for inactive users and redirecting to custom pages.

---

## **Class: CustomAccountAdapter**

This class extends `DefaultAccountAdapter` to customize Allauth behavior for account redirection and login.

---

### **Methods**

#### **1. `get_signup_redirect_url(request)`**
Redirects users to the **registration pending page** after successful signup.

- **Args**:
  - `request (HttpRequest)`: The HTTP request object.
- **Returns**:
  - `str`: The URL for the **registration pending page**.

---

#### **2. `get_login_redirect_url(request)`**
Redirects inactive users to the **registration pending page** instead of the default inactive page. Active users follow the default Allauth redirection logic.

- **Args**:
  - `request (HttpRequest)`: The HTTP request object.
- **Returns**:
  - `str`: The URL for the appropriate login redirection.

---

#### **3. `login(request, user)`**
Prevents auto-login for inactive users by checking their `is_active` status. Active users follow the default Allauth login process.

- **Args**:
  - `request (HttpRequest)`: The HTTP request object.
  - `user (User)`: The user instance being logged in.
- **Returns**:
  - `None`.

---

</details>