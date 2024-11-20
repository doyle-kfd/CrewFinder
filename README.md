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
  - AC-2 Admin can approve or disapprove accounts with a single click.
  - AC-3 Approved users are notified and gain access to the platform to complete their profile; disapproved users receive a notification.

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
