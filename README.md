# F1 Blog

<img src="https://i.imgur.com/VFVFeCF.png">

---
## Introduction

F1 Blog is a blog about.... well F1, where users can view race summaries, discuss whats happening in F1 world, their opinions on the races and basically anything F1 related.

This project was developed as part of CI's 16 week Full Stack Development course as final individual project, bringing together the knowledge I've learned over the course through my study.

The project focuses on the use of Django and Bootstrap frameworks to aid in the production of a functional web app with database manipulation and CRUD functionality.

<h4 align="center">[You can view the deployed site by clicking on this](https://f1-blog-127d4f6de80c.herokuapp.com)</h4>

## Overview

This was designed for everyone no matter how long have they been in touch with f1, from novice fan to a more experienced and knowledgable ones.

The idea was to make a site that utilises implementation of CRUD functionality in short time (few weeks) while still retaining a relevant use case.

In this regard, F1 blog (real inspiring name, ikr?) is a place to users to gather and to post their opinions on the races, discuss the latest news and share their thoughts on the sport.

Users on site can do the following:

- Register, log-in and log-out
    - _(Login required to view, post comments, post articles)._
- Post/Edit/Delete Comments
    - _(Users can post/edit/delete comments under race specific blog posts (**only their own comments**))._
- Collaborations
    - _(If user wishes to collaborate in future for one of the upcoming races, they can do so via collaboration form in about page)._
- Contact
    - _(If user wishes to get in contact for whatever reason, they can do so via contact form on contact me page)._
- Edit their profile
    - _(Future implementation, planning on adding easily accessable user profile editing, such as: adding bio, ability to change user picture, ability to select favourite team/drivers/circuits etc.)._
- Embed options
    - _(Users can easily share their specific race blog posts (or even a landing page) and they will be embedded with title, description and picture (**compact view**))._
---
## User Stories

Below are some of the user stories can be found in GitHub Projects board, which was used to add/edit and track progress completion

### User not logged-in:
| I want to | acceptance criteria |
| ------ | ------ |
| Create a account so that I can log in | 1. User can log-in to account they registered. <br> 2. User can log-in. 3. User can log-out. |
| Browse available blogs | 1. Users can view the individual race blogs available on site. <br> 2. Not logged-in users can view individual blogs and request to contact/collablorate. To leave comments they need to be logged in. |
| | |

### User Logged-in:
| I want to | acceptance criteria |
| ------ | ------ |
| Log in and log out of my account | 1. Users can log in to account they registered. <br> 2. Users can log out of their account. |
| Browse available blogs | 1. Users can view the individual race blogs available on site. |
| Post comments | 1. Users can post comments on the site. <br> 2. Users can see their comment posted on site (if approved by moderators) <br> 3. Comments that user posts (if approved) are visible to all logged-in users, underneath individual race blog post. |
| Being able to edit or delete comments | 1. Users can edit their comments. <br> 2. Users can delete their comments. |
| Easily navigate the site so I can find exactly what I'm looking for | 1. Users can easily navigate the site using nav bar or buttons at the bottom of pages. <br> 2. All relevant public pages on the site are accessible through links and are clearly labelled. |
| Being able to delete my account | 1. Users can delete their account. <br> 2. All items/things associated with user's account is deleted. |

### Stories not in Scope for first release:
| I want to | acceptance criteria |
| ------ | ------ |
| I want to be able to search for specific blog posts | 1. Users can click on search box and search for desired race blogs. <br> 2. Users can filter out search results by gp's names, years, authors, teams. |
| I want to be able to like or dislike comments | 1. Users can like or dislike comments <br> 2. Users can undo the likes or dislikes given to specific comment.
| I want to be able to edit my profile | 1. Users can edit their profile (such as adding profile pictures, bio's, select favourite team/drivers/circuits).
| I want to be able to favourite blog posts | 1. Users can favourite certain blog posts, which would show up in their profile as favourited. | <br> 2. Users can unfavourite posts. |
| I want to be able to link my social media profiles to my website account | 1. Users being able to link their existing accounts to website account. |

---
## Workflow and Methodologies
---
- In this project, I successfully applied Agile Methodology, incorporating the MOSCOW prioritization workflow. Leveraging my prior experience with these workflows and methodologies from Hackathon projects, I was able to effectively adapt them to an individual project, reaffirming their value in this context:

- The development of my ERD and Wireframes, in conjunction with the Agile Methodology, prompted me to critically evaluate the essential features of my project. By creating tasks based on a comprehensive set of user stories, I was able to adopt a user-centric approach, ensuring that I was prioritizing features that truly met the needs of my target audience.

- Throughout the project, regularly reviewing my board and decomposing each segment into manageable tasks enabled me to maintain a clear understanding of my current workload and plan my next steps. This approach allowed me to stay focused, make steady progress, and seamlessly transition between tasks as I completed them.

- Effective planning and management of my Kanban board from the outset enabled me to establish a robust timeline and maintain a tight scope, thereby preventing unnecessary deviations and ensuring that I stayed on track to meet my project deadlines.

![Project Board](https://i.imgur.com/yXJUq4c.png)

- By leveraging Labels, I successfully applied the MOSCOW prioritization method to each user story, allowing me to visualize and track their priority levels within my Project Kanban board. This enabled me to easily access and adjust the priorities as needed, ensuring that I remained adaptable to changing project requirements and timelines.

<p align="center"><img src="https://i.imgur.com/TxdokJL.png"></p>

You can find project board within the "projects" section of this Github Repo.

---
## Ideation

### Project Features
- Users can create an account and log in to the site.
- Users can browse available blogs.
- Users can post comments on the site.
- Users can edit or delete their comments.
- Users can easily navigate the site using nav bar or buttons at the bottom of pages.
- All relevant public pages on the site are accessible through links and are clearly labelled.
- Users can delete their account.


### Project Extra features
- Users can easily share their favourite blog posts across any social media of their choosing and it will be embedded in compact view (heading, description and picture) which can be seen below
Homepage embed
<p align="center"><img src="https://i.imgur.com/PqLjLmg.png"></p>
Article embed
<p align="center"><img src="https://i.imgur.com/Jz7ySoK.png"></p>
---

### Models

#### Built In
##### User/User Registration
- User Registration and log in was handled with Django's built in User Model in combination with Django AllAuth.

#### Custom Models
##### Contact Model
| Name | Type |
| ----- | ----- |
| Name | Charfield |
| Email | Emailfield |
| Message | Textfield |
| Read | BooleanField |

### Visual Design

#### Colour Scheme

The color scheme of the site is loosely based off real F1 site and a palette I discovered on https://www.brandcolorcode.com/formula-one

<p align="center"><img src="https://i.imgur.com/PVbde2N.png"></p>

- For site I wanted to go with 'original' but tweaked design with dark gray being contrasting color to white, giving it it a nice colour palette with a touch of bright red.
- Red (and white less so) is commonly associated with many companies, one of the being Formula 1. The site revolves around F1 so it made sense that white and red are found on the site

#### Font

For the font of choice I kept it simple and went with Sans Serif, however future implementations could use F1's font (you can actually find the original ones with inspect element on their website (downloads automatically when you click the link) or use similar fonts):

- https://www.formula1.com/etc/designs/fom-website/fonts/F1Regular/Formula1-Regular.ttf

- https://www.formula1.com/etc/designs/fom-website/fonts/F1Bold/Formula1-Bold.ttf

- https://www.formula1.com/etc/designs/fom-website/fonts/F1Wide/Formula1-Wide.ttf

- https://www.formula1.com/etc/designs/fom-website/fonts/F1Black/Formula1-Black.ttf

- https://imjustcreative.com/download-f1-fonts-formula-1-fonts/2021/09/16

---
## Site Showcase

First picture is a landing page (desktop)

![Homepage desktop](https://i.imgur.com/1uKnEdF.png)

Secondly we have a landing page (phone)

![Homepage phone](https://i.imgur.com/Rhh97v4.png)

thirdly we have a login page (desktop)

![login](https://i.imgur.com/Z36Cy99.png)

Next we have a about page (desktop)

![About](https://i.imgur.com/KUEBwRJ.png)

One of the posts (desktop)

![One of the posts](https://i.imgur.com/fk5bzlT.png)

One of the posts (mobile)

![One of the posts](https://i.imgur.com/YVsYpY7.png)

---
## Future Implementations

There were several features during the initial ideation of the project that had to be cut based on scope and timing considerations. A couple others were cut during production due to time constrains for features that were lower down on the MOSCOW prioritisation.

### Further down the road


- In future, I'd like to add more updates with events happening around F1 (this includes more details from races, activities F1 drivers are involved in which are for good causes but not necessarly revolve around the track)

- As a nerd myself, I'd like to implement comperhensive statistics (you know, all the data from each car per session, track data etc.) so you can see how each car behaves and what to expect from future upgrades teams bring

- I would like to add some social features, such as: comment replying, comment and post liking, photo/videos to be posted in comments, favouriting posts, being able to edit user profile etc.

- Post searching, simply to be able to search for posts for easier finding

- Password resetting/social account login (oauth)

## Compatibility/accessibility

### Device compatibility & responsivness

As demonstrated above in the site showcase and Project introduction image, site has been fully responsively tested to ensure that nothing breaks based on screen sizes down to 240px in width, which is more than widely accepted (320px) as the key mobile display width range to aim for. 

Throughout the sites development, no significant changes were made to ensure that all device widths were compatible, although Bootstrap does a very solid job in assisting with this out of the box.

- Ensured all elements were viewable and did not break or overflow from large resolutions, all the way down to 240px.
- Ensured pagination options were a decent size and still easily clickable on Mobile devices.
- Ensured a responsive navbar was implemented and that all dropdown options functioned.
- Ensured that elements scaled responsively while retaining readability.

### Accessibility

To ensure accessibility, I implemented several key features. I added appropriate ARIA labels to page elements, enabling seamless functionality with screen readers. Furthermore, I designed buttons to be clearly visible and included informative messages to notify users of actions taken, promoting a more inclusive user experience.

## Technologies used
- HTML
- CSS
- Python
- Javascript
- Git - Version control
- Visual Studio Code - i choose this over gitpod since it would make sense in real world environment
- GitHub - Storage and management of code repository
- GitHub Projects - Task Management and Agile workflow implementation
- Django - Python Framework used as core pillar of project
- Bootstrap - Framework for HTML elements
- Cloudinary - Cloud-based media storage
- ElephantSQL - Free option to host PostgresSQL database for the project
- Heroku - Host the deployed Moteify app site
- Photoshop - Main display image
- Code Institute CI Python Linter - Python Manual Testing
- W3 Markup Validation Service - HTML & CSS Validation Testing

## Libraries and Frameworks
- Bootstrap v5.3.2
- Django v 4.2.1
- Django AllAuth v0.57.0
- Django Crispy Forms v2.0
- Django-summernote v0.8.20.0
- Crispy Bootstrap v0.7
- Whitenoise v6.5.0
- Gunicorn v20.1.0
- Cloudinary v1.36.0

## Additional tools
- Autopep8 - Python Formatter
- GoogleFonts - Fonts
- Imgur - ReadME image hosting
- ChatGPT - Debugging and documentation assistance

---
### Deployment

Django & Heroku Deployment was set up following the PDF provided by CI below:
[Deployment Guide](Deployment.pdf)

### Credits & references
- [Django Documenation](https://www.djangoproject.com)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Code Institute](https://codeinstitute.net/ie/) - CI's Bootcamp Course Learning Platform content was referenced often during the project.
- [ChatGPT](https://chat.openai.com) - Used for troubleshooting, debugging, bugfixing, and breaking down challenging concepts into easier to understand info.
- [RaceFans](https://www.racefans.net/) - Used for all the F1 images
- [Formula 1](https://www.formula1.com/) - Used as inspiration for all the blog posts

### Acknowledgements

- I know there is no ERD, flow chart, wireframes, bug and validation documentation. I was short with time hence they aren't included in base release.

- I would like to thank *my colleagues* on *TIAS bootcamp* course. I've learned so many different things in such a short time span through hackathons and course lessons.

- I would also like to thank my mentor/facilitator *David Calikes*, who's support and commitment throughout this course was simply amazing. What a man! 

- Thanks to *CI* for prividing a unique opportunity to add many skills to my cv and bring me to the world of software development. Prior to this course, i was at the lowest point of my life. Now I'm looking forward to a brighter future in this ever evolving tech world

- Big thanks to *my family and my friends* for their support and encouragement throughout these challenging coding days.


