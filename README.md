# Test site Flask

This site will take the user input in the form page and it will show the data in the success page after validation.

## Architecture Overview

#### WordPress
WordPress is a CMS architecture built on PHP and MySQL. It comes with a pre-built database schema, admin dashboard, and plugin system designed primarily for content management and rapid site deployment.

#### Flask
Flask follows a micro-framework architecture built on Python. It is provids only the essentials (routing and requests) while allowing developers to custom-build the application and integrate any database or library.


### Overall structure
WordPress is strictly optimized for managing content like posts, pages, and metadatas. It is built specifically for MySQL or MariaDB. While Flask can connect to SQLite, PostgreSQL, MySQL, or NoSQL (like MongoDB).

## WordPress Design Decisions

### Layout Structure
WordPress layouts are structured into reusable components—typically a header, footer, and sidebar. WordPress uses a strict Template hierarchy.The design decision is to automatically load specific files based on the content type being viewed, ensuring a consistent layout structure across the site without manual routing.

### Reusability
WordPress uses a modular approach where common layout elements are stored in separate files.Nowadays WordPress, the Synced Patterns (formerly Reusable Blocks) system allows users to create a specific layout section such as 
- a call-to-action
- a team bio 
and use it across multiple pages.

## Application Implementation

### Form modification
I added the radio field, Date field and file upload field in the existing form with data validations.  When user will submit the data server will again validate the data and all the responses will be shown on the ```success.html``` page.

### Validation Logic
- No data will be submitted untill the user fills all the input fields
- The email field only accepts ```@gauhati.ac.in``` as email domain.
- Input Date must be in past.
- In the file upload user can only submit PDFs or Images

### UI improvements
Integrated Bootstrap CSS along with custom css to make the UI look better. Added Navbar and footer using Bootstrap templates.

## Security Considerations
### Input validation risk
With input validation user can input malicious code and make the website vulnerable to XSS Attacks. 
### File Upload risk
Uploading any file without filetype checks can lead to hacks and it can take much bandwidth and server storage if the filesize heavy.



----------
----------

# PART B

#### Q4
ans. to

- a. I will the allow both the pluging untill I test the plugin, if its breaking the UI or not. If its okay then i will allow only the Page builder plugin which may help the departments admin. But a heavy animation plugin may break the page loading time which may effect the users with low speed internet.

- b. Installing page builder without on the website upon the existing builder , it may break the CSS of existing pages. For the animation plugin, it may make the website beutifull but it will also increase the page loading time , which i will effect the UX.
