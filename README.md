# Javascript with JQuery Exercise - A Topic Of Interest To Me

Welcome! In this assignment, you will add Javascript code to a new page on your web site and use the JQuery framework to add interactive behaviors.

Any new or updated files required for your site to look and function correctly must be published to the web by uploading them within your web root directory on the web server.

The new Javascript file must be named `main.js` reside in a sub-directory named `js`. The JQuery file will also reside in this directory. Both Javascript files must be linked to from the new HTML document you make in this assignment.

## Requirements

Some rules about interactive behaviors for specific pages follow.

On top of these requirements, you are welcome to add any additional interaction you believe will make this page compelling and stimulating to someone finding it on the web.

### Copy existing web site files

The work you do in this assignment will be published to the same directory where your current web site currently exists. To prevent you from accidentally deleting any of your existing web site files, copy all the files from your existing web site into the main project directory for this assignment. This means copying any existing HTML, CSS, images, and other files and directories so a copy exists within this project directory. Then we will be able to upload everything in this directory to the web server and replace all existing files without worry about losing anything.

### Download JQuery

Before you begin, you will need to download a copy of JQuery's Javascript code.

1. Go to [jquery.com](https://jquery.com/)
1. Go to the Download page.
1. Click to download the "compressed" or "minified" version of the code.
1. Save that code into your project's `js` directory in a file named `jquery.min.js`. The exact file name may vary depending upon the version.
1. Do not modify the contents of this file.
1. Link to this file from HTML using a `<script>` element nested within the `<head>` element.

### Custom Javascript code

Create a new Javascript file named `main.js` within your project's `js` directory. This will hold any Javascript code you personally write as you complete this assignment. You will not modify Javascript code in any other file.

### Topic of interest

Create a new HTML document named `topic_of_interest.html`. As the name might suggest, this page will hold content about a topic of interest to you.

In the `<head>` of this file, the page must use `<script>` elements to instruct the web browser to load the two Javascript files: first load the file with the code you downloaded from JQuery, and then load your own `main.js` file.

This file must also load the site-wide CSS file you created in the previous assignment. Use a `<link>` element to load the external CSS. Feel free to write additional CSS to make this page beautiful and elegant.

Place any content about the topic of interest on this page. It is up to you to present the topic in a way that is interesting and engaging to others.

### Add custom interactive behaviors

By modifying the code in your HTML, CSS, and Javascript files, add interactive behaviors to this new page.

At a minimum, you must include the following event-driven behaviors using JQuery:

- **content change** - change the text content nested within any element (the 'target' element) on the page when the user performs a click, mouseover, or mouseout event on any other element of your choosing (the 'trigger' element)
- **image swap** - change the `src` attribute of any `<img>` element on the page (the 'target' element) when the user mouses over that same element in order to replace the original image with a new one. When the user mouses out of that `<img>` element, change the `src` attribute back so the original image is displayed again. With an image swap, the 'trigger' element and 'target' elements are one-and-the-same.
- **animation** - change the position on the page of any element on the page (the 'target' element) when the user performs a click, mouseover, or mouseout event on any other element of your choosing (the 'trigger' element). Do this by using JQuery's `animate()` function to adjust the target element's `left` and `top` properties. Note that the target element must have its `position` CSS property set to `relative` or `absolute` in order for this to work.

## Extra credit

For up to 10% extra, you may Incorporate another third party Javascript library. Some ideas:

- [scrollMagic](https://scrollmagic.io/) for animations controlled by the scroll bar
- the [Retina.js](https://imulus.github.io/retinajs/) library to offer images that are twice as large for high-resolution screens
- [VelocityJS](http://velocityjs.org/) to add more UI/UX effects like "shake",
- [soundJS](https://createjs.com/soundjs) to add sound to your site and web applications

When you submit your work, let us know if you have done the extra credit option.

## Submit your work

In order to submit this assignment, you must publish all modified files to the web and upload the code to GitHub.

### Upload the web page to a web server

Upload all files you have created to a web server. Your instructor will have given you instructions for how to do this.

Take note of the web address (URL) of your web page - this is the address that can be plugged into the address bar of any web browser for the web browser to load and display your web page.

### Update the settings.json file

Make sure your name, NYU Net ID, and the exact URL of your web site's home page are placed into the `settings.json` file in the appropriate places. Make sure the URL works when plugged into a web browser beforehand.

**Additional settings**
Additionally, you **must** add details about the interactive behaviors to the `settings.json` file. In particular, indicate the following in the appropriate places:

- CSS-style selectors for trigger and target elements involved in the **content change** behavior, as well as the type of trigger event that causes the content change to occur (i.e. mouseover, mouseout, or click).
- CSS-style selector for the image element involved in the **image swap** behavior.
- CSS-style selectors for trigger and target elements involved in the **animation** behavior, as well as the type of trigger event that causes the animation to occur (i.e. mouseover, mouseout, or click).

### Submit your work on GitHub

You are now ready to submit this assignment. You can do so directly from Visual Studio Code with the following steps, in the indicated order:

1. Switch to the Source Control view in Visual Studio Code - this view will show you a list of the files you have modified.
1. In the "`Message`" text field towards the top-left, enter a unique message to yourself about what you have changed and, while still with the text field selected, type `Command`-`Enter` on Mac OS X, or `Control`-`Enter` on Windows, to "commit" the changes you've made with this custom message. If you forget to hit `Command`-`Enter` after typing the message, you can instead click the "`...`" button above the message field and click the "`Commit all`" option in the menu that appears.
1. Now, click the "`...`" button above the message field and click the "`Push`" option in the menu that appears - this will upload your changes to your personal code repository on GitHub.

You have now submitted your completed assignment. Your changes are now posted to GitHub.com, where the instructor and graders can access it. Your `settings.json` file has information about who you are and where we can view your page on the web.

You can verify all this yourself manually by visiting your repository on GitHub.com and making sure the code displayed there is what you submitted.
