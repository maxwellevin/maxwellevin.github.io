---
title: Rubik Cube Solver
subtitle: A fun algorithms project involving a rubik cube and java. 
featured_image: /images/projects/rubik-cube/unsolved-cube.png
date: 2017-12-10 00:00:00
layout: project
---

This was a 2-week project I worked on with my friend and lab partner Journy Ma-Johnson during our Fall 2017 Algorithms class at Lewis & Clark College. We ambitiously decided to write a java program that shuffles a virtual rubik cube and then finds a sequence of moves that would solve the cube. 

![](/images/projects/rubik-cube/unsolved-cube.png)

The most challenging part of the project was writing code that would perform the 12 different rotations you can perform on the cube at any time. We used arrays to represent each face of the cube, and if we weren't exactly right with our rotation functions,then we could wind up with too many or too few pieces of a certain color. It took some JUnit testing and some handling of a physical rubik cube in order to make sure that each of our functions were air-tight. 

```java
/**
* Rotate the right side of the cube down.
* BlueSide rotates counterclockwise
* R red -> R yellow -> L orange -> R white -> R red
*/
public void iRightSideRotate() {
    rotateSideCounterClockwise(blueSide);
    int[] tempRed = {
        redSide[2][0], 
        redSide[2][1], 
        redSide[2][2]
    };
    for (int j = 0; j < 3; j++) {
        redSide[2][j] = whiteSide[2][j];
        whiteSide[2][j] = orangeSide[0][2 - j];
        orangeSide[0][2 - j] = yellowSide[2][j];
        yellowSide[2][j] = tempRed[j];
    }
}
```

Once that was out of the way, we performed a large number of rotations on a solved cube to shuffle it and set our iterative deepening depth-first search algorithm loose to see how quickly it could solve the cube. It was able to solve cubes that could be solved in less 8 moves in a few seconds but anything more than that and it seemed to take forever. This is partly because the search-space of a rubik cube is absolutely massive (There are 43 quintillion unique cubes), and our depth-first search algorithm wasn't optimized to trim this search space. However all Rubik Cubes can be solved in 20 moves or less, so this wasn't the only reason our depth-first search was ineffective at truly scrambled cubes. The main reason is that the search space grows exponentially with the depth of the depth-first search. Since we coded 12 unique moves, each layer in the search tree has 12^d elements in it. At a depth of just 10 (i.e. 10 moves from the starting position) there are nearly 62 billion cube positions, some of which are duplicates. 

Going forward I may look into algorithms that are better tailored to the rubik cube than iterative-deepening dfs. I'd love to make it able to solve any Rubik Cube very quickly. Once that it done, it could be fun to explore different ways of initializing the Rubik Cube. Maybe a simple GUI so you can set it how you want or something more complex, like processing a series of images of a real rubik cube.

To checkout the code see [github.com/maxwellevin/lclark-algorithms/RubiksCube](https://github.com/maxwellevin/lclark-algorithms/tree/master/Rubiks%20Cube).

