---
title: 'Sorting Hat'
subtitle: 'An automated course allocation program for Lewis & Clark College'
featured_image: '/images/projects/sortinghat/sortinghat_gui.png'
layout: page
---

## SortingHat 1.0 !


![](/images/projects/sortinghat/old_sortinghat_gui.png)


A version of this program was constructed in Spring 2018 by Lars Mayrand, Nick Tan, Mack Beveridge, Sam Peers, James Tostado, and I in a Software Development class at Lewis & Clark College. The application was built in Java and would allocate freshmen into their Exploration & Discovery (E&D) courses based on the following factors:
* Students must get one of their top three or four choices
* No class should have more students than the class can fit
* No student can take a course with a professor they have already had
* Gender ratios should be somewhat balanced in each class
* Athlete ratios should be somewhat balanced in each class

The thresholds for some factors (top choices, gender ratios, athlete ratios) were determined after meetings with the client. Other factors, such as the maximum class size for a given course, were provided in a csv file as inputs to the program. In addition, the program also had to account for students who had already been allocated a course manually (Our client wanted the ability to manually place certain students before the program ran) and the program needed to account for students who listed course preferences with a previous professor. 

The product delivered to Lewis & Clark College upon the end of the Spring 2018 term was able to allocate 500+ students to E&D sections in less than a tenth of a second while satisfying all of the above requirements. Previously this task took our client over a week to complete and it needed to be done every semester. This version of SortingHat has been used for two semesters so far and counting.

See the <a href="https://github.com/maxwellevin/sofdev-eandd-sortinghat">github repo</a> for SortingHat 1.0.



## SortingHat 2.0 

![](/images/projects/sortinghat/sortinghat_gui.png)

This version is in the process of being constructed by myself and SortingHat 1.0 teammate Lars Mayrand. The primary goal with SortingHat 2.0 is to increase the flexibility of the program so that it can be used by other academic institutions in need of allocation tools where student preference must be taken into account. 

To make this more accessible, I rewrote the project in Javascript (fixing some bugs along the way), and redesigned the user interface. Sliders were added to improve flexibility of existing parameters. The program runs in approximately five seconds (varies with user's computer specs), which is several times longer than the Java version, but still acceptable. 

Visit the <a href="https://github.com/1800Blarbo/SortingHat.org">github repo</a> for the new SortingHat to see more detailed documentation, tasks left to do, or submit a pull request.


![](/images/projects/sortinghat/sortinghat_demo.mov)
