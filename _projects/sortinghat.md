---
title: 'Sorting Hat'
subtitle: 'An automated course allocation program for Lewis & Clark College'
featured_image: '/images/projects/sortinghat/sortinghat_gui.png'
layout: page
---

SortingHat is a program designed to eliminate headaches and save time when assigning students to classes. 

There are two versions of SortingHat: 
- SortingHat 1.0 - the original, delivered as a .JAR app ([github repo](https://github.com/maxwellevin/sofdev-eandd-sortinghat))
- [SortingHat.org](http://www.SortingHat.org) - a refresh, delivered as a webapp ([github repo](https://github.com/1800Blarbo/SortingHat.org))

## SortingHat 1.0


![](/images/projects/sortinghat/old_sortinghat_gui.png)


A version of this program was constructed in Spring 2018 by Lars Mayrand, Nick Tan, Mack Beveridge, Sam Peers, James Tostado, and I in a Software Development class at Lewis & Clark College. The application was built in Java and would allocate freshmen into their Exploration & Discovery (E&D) courses based on the following factors:
* Students must get one of their top three or four choices
* No class should have more students than a specified limit
* No student can take a course with a professor they've already had
* Gender ratios should be somewhat balanced in each class
* Athlete ratios should be somewhat balanced in each class

The thresholds for some factors (top choices, gender ratios, athlete ratios) were determined after meetings with the client. Other factors, such as the maximum class size for a given course, were provided in a csv file as inputs to the program. In addition, the program also had to account for students who had already been allocated a course manually and account for students who listed illegal course preferences.

The product delivered to Lewis & Clark College upon the end of the Spring 2018 term was able to allocate 500+ students to E&D sections in less than a tenth of a second while satisfying all of the above requirements. Previously this task took our client over a week to complete each semester. This version of SortingHat has been used every semester since Spring 2018.

See the <a href="https://github.com/maxwellevin/sofdev-eandd-sortinghat">github repo</a> for SortingHat 1.0.



## SortingHat.org

![](/images/projects/sortinghat/sortinghat_gui.png)

This version is in the process of being constructed by myself and SortingHat 1.0 teammate Lars Mayrand. The primary goal with SortingHat 2.0 is to increase the flexibility of the program so that it can be used by other academic institutions in need of allocation tools where student preference must be taken into account. 

To make this more accessible, I rewrote the project in Javascript (fixing some bugs along the way), and redesigned the user interface. Sliders were added to improve flexibility of existing parameters. The program runs in just a few seconds (varies with the user's computer specs).

Additionally, I added several charts and more responsive feedback about the section and student data in order to give the user a better understanding of their data. For instance, see the <strong>Section Popularity</strong> chart:

![](/images/projects/sortinghat/popularity_chart.png)

Also notice the new <strong>Allocations</strong>, <strong>Gender Composition</strong>, and <strong>Athlete Balance</strong> charts which display the program's results after the user clicks the 'run' button.

![](/images/projects/sortinghat/allocation_chart.png)

![](/images/projects/sortinghat/gender_chart.png)

![](/images/projects/sortinghat/athlete_chart.png)


Visit the <a href="https://github.com/1800Blarbo/SortingHat.org">github repo</a> for the new SortingHat to read the documentation, browse the source code, or submit a pull request. 

You can also visit <a href="http://www.sortinghat.org">www.sortinghat.org</a> to see SortingHat live!


