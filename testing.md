# Testing Documentation

---

## Introduction

This is a page where all the tests are done. Alongside the explanations are all the screenshots showcasing what each test did and what the results are.
There are several categories which will be tested, and those tests include: Manual, Responsiveness, Code validation, User Story, Bug documentation.
There are several test case formats:
Expected (defined whats expected to happen) 
Testing (the steps used to do an action)
Result (recorded the outcome regardless of result)
Fix (if something didn't turn out as expected, figure out why and make said changes to make it work)

---

## Responsiveness Testing

site which was recommended (https://responsivedesignchecker.com/) didn't work due to [default setup of my site](https://i.imgur.com/gOXy9tE.png) (for privacy and security reasons | iframe embed issue), hence pics from built in tool from the browser will have to suffice:

[Desktop image](https://i.imgur.com/WYs1AGk.png)

[Laptop image](https://i.imgur.com/UdBabVr.png)

[Tablet image](https://i.imgur.com/ij8k41S.png)

[Phone image](https://i.imgur.com/0bIKzew.png)

## Code validation

### HTML and CSS Results

Used https://validator.w3.org for HTML and CSS testing

HTML


| Part | URL | Results |
| ----- | ----- | ----- |
| Home | [link](https://validator.w3.org/nu/?doc=https%3A%2F%2Ff1-blog-127d4f6de80c.herokuapp.com%2F) | multiple warnings and errors due to multiple *text-muted* being on the same page. This can be solved by having 2 articles per page |
| Register | [link]() | no issues |
| Sign In | [link]() | no issues |
| About | [link]() | no issues |
| Contact Me | [link]() | no issues |
| Sign Out | [link]() | multiple warnings and errors due to multiple *text-muted* being on the same page. This can be solved by having 2 articles per page |

*Merchandise* and *Watch Live* sites are from F1 themselvs. I have simply [link]ed them to my page. I will not explain issues in detail since there are many, [link] to test will still be provided non the less.

| Merchandise | ----- | 217 total issues, most are labeled as info. Had to validate by view page source as it would just timeout if you paste the [link]. |
| Watch Live | [link](https://validator.w3.org/nu/?doc=https%3A%2F%2Ff1tv.formula1.com%2F) | 16 total issues, all of them are info's |

CSS

| Part | URL | Results |
| ----- | ----- | ----- |
| base.css | [link] | no errors found, 216 warnings |
| style.css | [link] | no errors found, 4 warnings |

*style.css has to be validated by direct input, hence the picture*

### JavaScript

Used https://codebeautify.org/jsvalidate for JS testing

| URL | Results | Additional |
| ----- | ----- | ----- |
| [link]() | 2 errors (validated by url) | errors on lines 1 (extra space) and 3 (Expected '(end)' and instead saw ') |

*since website doesn't support sharing results as links, picture of results will be shown above*

### Python

PY

| File | Results | Additional |
| ----- | ----- | ----- |
| about: admin.py |  | no issues |
| about: apps.py |  | no issues |
| about: forms.py |  | no issues |
| about: models.py |  | no issues |
| about: test_forms.py |  | no issues |
| about: test_views.py |  | no issues |
| about: tests.py | no issues | image not included due to file being basically empty |
| about: urls.py |  | no issues |
| about: views.py |  | no issues |

| blog: admin.py |  | no issues |
| blog: apps.py |  | no issues |
| blog: forms.py |  | no issues |
| blog: models.py |  | no issues |
| blog: test_forms.py |  | no issues |
| blog: test_views.py |  | no issues |
| blog: tests.py | no issues | image not included due to file being basically empty |
| blog: urls.py |  | no issues |
| blog: views.py |  | no issues |

| contact: admin.py |  | no issues |
| contact: apps.py |  | no issues |
| contact: forms.py |  | no issues |
| contact: models.py |  | no issues |
| contact: test_forms.py |  | no issues |
| contact: test_views.py |  | no issues |
| contact: tests.py | no issues | image not included due to file being basically empty |
| contact: urls.py |  | no issues |
| contact: views.py |  | no issues |

## User Story

| Name | Criteria | Result |
| ----- | ----- | ----- |
| Merchandise support | Have integrated merch site | Pass |
| Drafting | Be able to draft comments | Pass |
| Comment moderation | Be able to moderate comments | Pass |
| About | Have an about page | Pass |
| Account creation | Being able to create account | Pass |
| Comments | Being able to comment | Pass |
| Editing/deletion of comments | Be able to edit/delete comments | Pass |
| Viewing comments | Be able to see commnets | Pass |
| Collaboration | Be able to submit collaboration form | Pass |
| Collaboration form storage | collab forms being stored | Pass |
| Contact | Have a way to contact admin | Pass |
| Contact form storage | contact forms being stored | Pass |
| Watch Live | being able to watch live races | Pass |

## Manual Testing
### Unregistered user
| Part | Action | Expected Outcome | Result |
| ----- | ----- | ----- | ----- |
| Navbar | Click *logo* (f1 text at very top left) | links to homepage | Pass |
| Navbar | Click "Home" | links to homepage | Pass |
| Navbar | Click "Merchandise" | links to merchandise page | Pass |
| Navbar | Click "Watch Live" | links to watch live page | Pass |
| Navbar | Click "About" | links to about page | Pass |
| Navbar | Click "Contact Me" | links to contact me page | Pass |
| Navbar | Click "Register" | links to register page | Pass |
| Navbar | Click "Login" | links to login page | Pass |
| Sign up | Fill out fields with valid info, press "sign me up" | User is signed up, logged in and back to homepage | Pass |
| Sign up | Click "Already have an account? Please [sign in] instead" | links to login page | Pass |
| Login | Enter correct details and press "sign me in" | Redirects to homepage | Pass |
| Login | Click "If you haven't created an account yet, then please [sign up] first" | links to sign up page | Pass |
| Article | Click on aricle | links to specific article | Pass |
| Footer | Click on author of the site | Redirects to author's GitHub | Pass |
| Footer | Click on social media icons | links to different social media's in new tabs | Pass |

### Logged-in user
| Part | Action | Expected Outcome | Result |
| ----- | ----- | ----- | ----- |
| Navbar | Click *logo* (f1 text at very top left) | links to homepage | Pass |
| Navbar | Click "Home" | links to homepage | Pass |
| Navbar | Click "Merchandise" | links to merchandise page | Pass |
| Navbar | Click "Watch Live" | links to watch live page | Pass |
| Navbar | Click "About" | links to about page | Pass |
| Navbar | Click "Contact Me" | links to contact me page | Pass |
| Navbar | Click "Logout" | links to logout page | Pass |
| Logout | Click "sign me out" | Signs out user | Pass |
| Article | Click on aricle | links to specific article | Pass |
| Article | Click on comment "body" | Type the commnet, press "submit" | Pass |
| Article | Click on "edit comment" | Edit the comment, press "submit" | Pass (if comment is approved) |
| Article | Click on "delete comment" | Deletes the comment | Pass (if comment is approved) |
| Footer | Click on author of the site | Redirects to author's GitHub | Pass |
| Footer | Click on social media icons | links to different social media's in new tabs | Pass |

## Bug documentation

This part is empty since I didn't encounter many big bugs worth sharing (didn't bother since all were small mistakes such as typos.)