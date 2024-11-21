# TESTING

- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  - [HTML](#html)
  - [CSS](#css)
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

## User Story Testing

#### EPIC | User Registration, Approval And Authentication
  - As a user, I want to register for an account with the option to select my role as either a captain or a crew member so that I can specify my participation in trips.
<p align="center">
  <img src="docs/testing/Signup form.png" alt="Signup Form" width="45%" style="margin-right: 10px;">
  <img src="docs/testing/registration pending.png" alt="Registration Pening Message" width="45%" style="margin-left: 10px;">
</p>

    - AC-1 The registration form includes fields for username, email, password, and role selection.
    - AC-2 Role selection is limited to "Captain" or "Crew. With the addition of Administrator for testing"
    - AC-3 After successful registration, the user sees a message indicating that their account is pending admin approval.


- As an admin, I want to review new account registrations and approve or disapprove them so that only validated users can access the platform.

<p align="center">
  <img src="docs/testing/admin panel.png" alt="Adminstrator Dashboard" width="45%" style="margin-right: 10px;">
  <img src="docs/testing/admin user approval.png" alt="Admin User Approval" width="45%" style="margin-left: 10px;">
</p>

    - AC-1 Admin dashboard lists all pending accounts.
    - AC-2 Approved users are notified and gain access to the platform to complete their profile; disapproved users receive a notification.
      - User receives email at address provided, updating status changes

- As an approved user, I want to complete my profile by adding information about my experience level and a bio, so that others can understand my skills and background.

<p align="center">
  <img src="docs/testing/complete profile.png" alt="complete profile" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 After admin approval, the user gains access to the profile setup page.
    - AC-2 The profile form includes fields for experience level and a bio.
    - AC-3 Form is styled using Crispy Forms and Bootstrap.
    - AC-4 Data saves successfully to the profile, and changes are visible on the dashboard.


- As an approved user, I want to view my profile on my dashboard, so I can see the information I’ve shared and make updates as needed.

<p align="center">
  <img src="docs/testing/updated my profile.png" alt="update profile" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 Dashboard displays user profile with fields for bio and experience level.
    - AC-2 The Edit option is available to update profile details.
    - AC-3 Changes save and update immediately upon submission.

- As a returning user, I want to log in and log out of my account securely to access my profile and trip features.

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <img src="docs/testing/login page.png" alt="Login Page" width="45%">
  <img src="docs/testing/user dashboard.png" alt="User Dashboard" width="45%">
</div>


    - AC-1 The login form includes fields for email/username and password, with clear labels for each.
    - AC-2 Upon successful login with valid credentials, the user is redirected to their dashboard.
    - AC-3 A Logout link is available in the navigation bar when the user is logged in.
    - AC-4 Upon logging out, the user is redirected to the homepage.
    - AC-5 If a logged-out user tries to access a restricted page (e.g., dashboard or profile), they are redirected to the login page.


#### EPIC | Trip Management

- As a captain, I want to create a sailing trip with details like title, location, date, and the number of crew needed, so I can recruit crew members for specific journeys.

<p align="center">
  <img src="docs/testing/create trip form.png" alt="create trip form" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 The trip creation form is only accessible to users with the "Captain" role.
    - AC-2 Form includes fields for title, location, date, and crew needed.
    - AC-3 Created trip appears on the captain’s dashboard under "My Trips."


- As a captain, I want to view a list of my created trips, so I can manage my upcoming trips and review participant status.

<p align="center">
  <img src="docs/testing/captains dashboard.png" alt="captains dashboard" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 Dashboard lists all trips created by the captain, sorted by date.


- As a captain, I want to view detailed information about each trip I create, including a list of crew members who have joined, so I can manage and organize my crew effectively.

<p align="center">
  <img src="docs/testing/captains dashboard.png" alt="captains dashboard" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 The Trip Details page displays trip information and a list of confirmed crew members.
    - AC-2 Option to approve or reject crew requests (if applicable).


#### EPIC | Joining Trips

- As a crew member, I want to view a list of available sailing trips, so I can decide which ones I’d like to join.

<p align="center">
  <img src="docs/testing/sailing opportunities.png" alt="sailing opportunities" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 Page that  displays a list of trips with open crew positions.
    - AC-2 Each trip entry includes title, location, date, and an option to request to join.

- As a crew member, I want to request to join a specific sailing trip, so I can participate and gain more experience.

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <img src="docs/testing/apply trip.png" alt="apply for trip" width="30%">
  <img src="docs/testing/trip pending.png" alt="Trip Pending" width="30%">
  <img src="docs/testing/trip confirmed.png" alt="Trip Confirmed" width="30%">
</div>

    - AC-1 The join request option is available for crew members on the trip details page.
    - AC-2 Request updates the trip’s participant list as "Pending."
    - AC-3 Confirmation of successful join request appears on-screen.


- As a crew member, I want to view the trips I’ve joined on my dashboard, so I can keep track of my participation.

<p align="center">
  <img src="docs/testing/crew dashboard.png" alt="crew dashboard" width="50%" style="margin-right: 10px;">
</p>

    - AC-1 Dashboard includes a "My Trips" section listing trips the user has joined.
    - AC-2 Trip status (e.g., Pending, Confirmed) displays for each entry.

- As a user, I want my experience to be tailored based on my role (captain or crew), so I only see actions and views relevant to my role.

  - AC-1 Captains have access to trip creation, management, and crew approval features.
    - Working
  - AC-2 Crew members have access to trip browsing and join request features.
    - Working
  - AC-3 Unauthorized users are redirected if attempting restricted actions.
    - Working

  #### EPIC | Role Based Access Control

  - As an admin, I want to manage user roles effectively, so I can control access to specific features.

    - AC-1 The admin panel includes options to view and modify user roles.
      - Working
    - AC-2 Role changes are saved and take immediate effect on user permissions.
      - Working

  - As a user, I want my experience to be tailored based on my role (captain or crew), so I only see actions and views relevant to my role.

    - AC-1 Captains have access to trip creation, management, and crew approval features.
      - Working
    - AC-2 Crew members have access to trip browsing and join request features.
      - Working
    - AC-3 Unauthorized users are redirected if attempting restricted actions.
      - Working


#### EPIC | Platform UI And Testing

- As a user, I want rich-text capabilities in my profile bio, so I can add more detailed information about myself.

  - AC-1 Bio field on the profile form supports rich-text formatting via Summernote.
    - Working, once approved user on first login has to complete bio.
  - AC-2 Bio content displays properly in the profile view on the dashboard.
    - Working. Can be updated as necessary

- As a user, I want the platform to have a clean and intuitive layout with easy navigation, so I can find features and complete actions quickly.

  - AC-1 Consistent styling across pages using Bootstrap and Crispy Forms.
    - Bootstrap and Cripsy formas have been implemented
  - AC-2 Navigation bar with links to key sections (dashboard, profile, trips).
    - Appropriate Navigation Is Available at all times
  - AC-3 All pages are mobile-friendly and responsive.
    - All pages tested for responsive design

#### EPIC | Static Pages

- As a visitor, I want an "About Us" page that describes the purpose of CrewFinder and the benefits of joining, so I can learn more about the platform.

  - AC-1 About Us page includes information on CrewFinder’s mission, team, and features.
    - All features visible
  - AC-2 Page is accessible from the navigation bar for all users.
    - Page Is Accessible from nav bar

- As a visitor, I want to see a welcoming home page that provides an overview of the CrewFinder platform, so I can understand the purpose and features of the app.

  - AC-1 Home page includes a brief description of CrewFinder, a call-to-action to join, and links to key pages (About Us, Sailing Opportunities, Contact Us).
    - Home page has hero introduction to set the scene with cta, then sections to help user buy into the site theme.
  - AC-2 Accessible from the navigation bar and visible to all users, including non-logged-in visitors.
    - Navigation is available to all users. Specific nav only accessible to logged in users

- As a visitor, I want a "Contact Us" page where I can find information on how to reach CrewFinder’s team, so I can ask questions or get support.

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <img src="docs/testing/contact us form filled in.png" alt="contact form filled in" width="30%">
  <img src="docs/testing/success message on sending .png" alt="success message on sending" width="30%">
  <img src="docs/testing/message from contact us page.png" alt="Email message from contact page" width="30%">
</div>

    - AC-1 Contact Us page includes a contact form with fields for name, email, and message, along with any relevant contact details.
      - Contact form has all necessary fields for filling in. Includes contact details.
    - AC-2 Submitting the form sends a message to the CrewFinder team and displays a confirmation to the user.



#### EPIC | Dynamic Pages

- As a visitor, I want to see a welcoming home page that provides an overview of the CrewFinder platform and displays the three latest trips, so I can see current opportunities and understand the purpose of the app.

  - AC-1 Home page includes a description of CrewFinder and links to key pages (About Us, Sailing Opportunities, Contact Us).
    - Complete and working
  - AC-2 The three latest trips are displayed dynamically, showing title, location, date, and a link to the trip details.
    - Complete and working
  - AC-3 Accessible from the navigation bar and visible to all users, including non-logged-in visitors.
    - Complete and working

- As a visitor, I want to view a "Sailing Opportunities" page with a list of all available trips, so I can browse sailing options before signing up.
  
  - AC-1 Sailing Opportunities page lists all active trips, showing titles, locations, dates, and number of crew needed.
    - Complete and working

- As a visitor, I want a login page where I can enter my credentials to access the platform, so I can reach my account and profile.

  - AC-1 Login page includes fields for email/username and password, along with a “Forgot Password?” option.
    - Complete and working
  - AC-2 Successful login redirects to the user dashboard.
    - Complete and working

  ## Validator Testing

  ### HTML

  ### CSS
