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

  - AC-1 Dashboard displays a list of trips with open crew positions.
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
  - AC-2 Each trip links to a detailed trip page where registered users can request to join (crew) or manage participation (captains).

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