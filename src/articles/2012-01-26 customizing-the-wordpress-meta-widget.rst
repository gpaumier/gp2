.. title: Customizing the WordPress meta widget
.. slug: customizing-the-wordpress-meta-widget
.. date: 2012-01-26 16:07:18
.. tags: WordPress,Coding,Engineering,Wikimedia
.. description: 
.. excerpt: How to customize the standard WordPress meta widget to add or remove stuff.

*`Jump to the code <#Code>`__ if you're not interested in the backstory.* I maintain the `Wikimedia Blog <https://blog.wikimedia.org>`__, and we wanted to include a link to our `posting guidelines <https://meta.wikimedia.org/wiki/Wikimedia_Blog/Guidelines>`__ to the "meta" section of our sidebar. There is no straightforward way to do this; the widget can't be edited from within the admin area. One possibility was to replace the standard meta widget by a custom text widget, with the same content and links, and to add our guidelines to the mix. But this meant losing the nice context-aware links (e.g. "Register" vs. "Site admin", and "Log in" vs. "Log out", respectively for logged-out and logged-in users) provided by built-in WordPress functions (``wp_register`` and ``wp_loginout``): widget text can't embed PHP code. Another possibility was to install a third-party plugin to customize the meta widget (or allow PHP code in widget text). I'm usually reluctant to using plugins for simple changes like the one we wanted to do. Both our Operations staff and I prefer to keep the amount of third-party plugins installed on the blog to a minimum, for various reasons (security, maintenance, maintainability, etc.) Because there are no hooks to plug into the widget's behavior, most of the solutions I've seen online consist either of using a third-party plugin, or messing with WordPress core files, which is a no-go for me. The third possibility, which is the one I went for, was to create our own meta widget. This is what the code below does. |Screenshot of the custom meta widget with a link to posting guidelines in the middle of the standard meta widget's content| Result: Our blog guidelines inserted into the meta widget. I used the `WordPress widgets API <https://codex.wordpress.org/Widgets_API>`__ to create a widget, as well as the content of the standard meta widget, located in ``wp-includes/default-widgets.php``. The code is located in our ```WMBlog`` plugin <https://github.com/gpaumier/WMBlog>`__, a set of customizations specific to our blog that work independently of the theme. The custom widget replicates the functionality of the standard meta widget (with the handy context-aware links) and also includes the link to our guidelines. It was a bit more work, but it's cleaner and more robust that way. Once the widget is available, an admin can replace the standard widget with the custom one. If you want to add stuff to the meta widget, or remove some of its standard content, this is probably the Right™ Way to do it. You'll want to look at lines 42 to 51 in the code below. Note: The code hasn't been deployed to production yet; it'll appear on the Wikimedia blog in a few days.

Code
====

\`\`\`php ); echo $before\_widget; if ( !empty( $title ) ) { echo $before\_title . $title . $after\_title; } ?>

-  
-  `Blog guidelines <//meta.wikimedia.org/wiki/Wikimedia_Blog/Guidelines>`__
-  RSS'); ?>
-  RSS'); ?>
-  `WordPress.org <http://wordpress.org/>`__

.. |Screenshot of the custom meta widget with a link to posting guidelines in the middle of the standard meta widget's content| image:: //guillaumepaumier.com/wp-content/uploads/2013/04/WMBlog-meta-widget.png
   :target: //guillaumepaumier.com/wp-content/uploads/2013/04/WMBlog-meta-widget.png
