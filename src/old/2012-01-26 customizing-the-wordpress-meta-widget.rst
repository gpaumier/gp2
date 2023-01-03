.. title: Customizing the WordPress meta widget
.. category: articles-en
.. slug: customizing-the-wordpress-meta-widget
.. date: 2012-01-26 16:07:18
.. keywords: WordPress, Coding, Engineering, Wikimedia
.. image: /images/2012-01-26_wmblog_widget.png
.. image-caption: Obligatory tilted illustration of part of the code


.. highlights::

    I recently had to investigate how to customize the “meta” widget provided by WordPress. I couldn’t find a good how-to at the time, so I wanted to share how I did it, in case other people needed to do the same.


.. note::
    `Jump to the code <#code>`__ if you're not interested in the backstory.

I maintain the `Wikimedia Blog <https://blog.wikimedia.org>`__, and we wanted to include a link to our `posting guidelines <https://meta.wikimedia.org/wiki/Wikimedia_Blog/Guidelines>`__ to the "meta" section of our sidebar.

There is no straightforward way to do this; the widget can't be edited from within the admin area. One possibility was to replace the standard meta widget by a custom text widget, with the same content and links, and to add our guidelines to the mix. But this meant losing the nice context-aware links (e.g. "Register" vs. "Site admin," and "Log in" vs. "Log out," respectively for logged-out and logged-in users) provided by built-in WordPress functions (``wp_register`` and ``wp_loginout``): widget text can't embed PHP code.

Another possibility was to install a third-party plugin to customize the meta widget (or allow PHP code in widget text). I'm usually reluctant to using plugins for simple changes like the one we wanted to do. Both our Operations staff and I prefer to keep the amount of third-party plugins installed on the blog to a minimum, for various reasons (security, maintenance, maintainability, etc.).

Because there are no hooks to plug into the widget's behavior, most of the solutions I've seen online consist either of using a third-party plugin, or messing with WordPress core files, which is a no-go for me. The third possibility, which is the one I went for, was to create our own meta widget. This is what the code below does.

.. figure:: /images/2012-01-26_WMBlog_meta_widget.png
    :alt: Screenshot of the custom meta widget with a link to posting guidelines in the middle of the standard meta widget's content
    :figclass: aside

    Result: Our blog guidelines inserted into the meta widget.


I used the `WordPress widgets API <https://codex.wordpress.org/Widgets_API>`__ to create a widget, as well as the content of the standard meta widget, located in ``wp-includes/default-widgets.php``. The code is located in our |plugin|_, a set of customizations specific to our blog that work independently of the theme.

.. |plugin| replace:: ``WMBlog`` plugin

.. _plugin: https://gerrit.wikimedia.org/r/#/admin/projects/wikimedia/communications/WMBlog,branches

The custom widget replicates the functionality of the standard meta widget (with the handy context-aware links) and also includes the link to our guidelines. It was a bit more work, but it's cleaner and more robust that way. Once the widget is available, an admin can replace the standard widget with the custom one.

If you want to add stuff to the meta widget, or remove some of its standard content, this is probably the Right™ Way to do it. You'll want to look at lines 42 to 51 in the code below.

Note: The code hasn't been deployed to production yet; it'll appear on the Wikimedia blog in a few days.


Code
====

.. code:: php

    <?php
    /*
       Replicate the default meta widget and extend it to include
       a link to the Wikimedia blog guidelines
       See https://codex.wordpress.org/Widgets_API for reference */

    class WMBlog_meta_widget extends WP_Widget {

      function WMBlog_meta_widget() {
        // (constructor) Instantiate the parent object
        parent::WP_Widget( /* Base ID */'WMBlog_meta_widget', /* Name */'WMBlog_meta_widget', array( 'description' => 'The default meta widget plus Wikimedia-specific stuff' ) );
      }

      function form( $instance ) {
        // output the options form on admin
        // i.e. for now only the widget's title
        if ( $instance ) {
          $title = esc_attr( $instance[ 'title' ] );
        }
        else {
          $title = __( 'New title', 'text_domain' );
        }
        ?>
        <p>
        <label for="<?php echo $this->get_field_id('title'); ?>"><?php _e('Title:'); ?></label>
        <input class="widefat" id="<?php echo $this->get_field_id('title'); ?>" name="<?php echo $this->get_field_name('title'); ?>" type="text" value="<?php echo $title; ?>" />
        </p>
        <?php
      }

      function update( $new_instance, $old_instance ) {
        // process widget options to be saved
        $instance = $old_instance;
        $instance['title'] = strip_tags($new_instance['title']);
        return $instance;
      }

      function widget( $args, $instance ) {
        // output the content of the widget
        extract( $args );
        $title = apply_filters( 'widget_title', $instance['title'] );
        echo $before_widget;
        if ( !empty( $title ) ) { echo $before_title . $title . $after_title; } ?>
          <ul>
          <?php wp_register(); ?>
          <li><?php wp_loginout(); ?></li>
          <li><a href="//meta.wikimedia.org/wiki/Wikimedia_Blog/Guidelines" title="General contribution guidelines for the Wikimedia blog">Blog guidelines</a></li>
          <li><a href="<?php bloginfo('rss2_url'); ?>" title="<?php echo esc_attr(__('Syndicate this site using RSS 2.0')); ?>"><?php _e('Entries <abbr title="Really Simple Syndication">RSS</abbr>'); ?></a></li>
          <li><a href="<?php bloginfo('comments_rss2_url'); ?>" title="<?php echo esc_attr(__('The latest comments to all posts in RSS')); ?>"><?php _e('Comments <abbr title="Really Simple Syndication">RSS</abbr>'); ?></a></li>
          <li><a href="//wordpress.org/" title="<?php echo esc_attr(__('Powered by WordPress, state-of-the-art semantic personal publishing platform.')); ?>">WordPress.org</a></li>
          <?php wp_meta(); ?>
          </ul>
        <?php echo $after_widget;
      }

    }

    function WMBlog_register_widgets() {
      // register the plugin's available widgets
      register_widget( 'WMBlog_meta_widget' );
    }

    // plug in the widgets registration
    add_action( 'widgets_init', 'WMBlog_register_widgets' );

    ?>
