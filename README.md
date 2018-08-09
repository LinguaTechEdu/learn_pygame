# Python Classroom Exercises

*Requirements*
1. Python 3
2. Pygame

Simple tasks to allow students to test new ideas on the spot that add up to a lesson.

Exercises were intended for a code-along and/or open workshop classroom format where students are coding throughout the lessons.

### TODO
Convert lessons to python 3:

- [ ] Bounce: Conditionals and Loops
- [ ] Text: Functions, arrays, string methods
- [ ] Sound: Loading sounds
- [ ] Square: Drawing and player movement
- [ ] Image: Loading images
- [ ] Guess: Operators, input, iteration
- [x] Draw: Algorithms, calculations

### How to Use

Each script is about 15-30 minutes of classroom material. Instructors should immediately demonstrate what the end game is for the students when they complete the script. Next, walk through each section of the script, not line by line -- section by section. Leave room for questions and exploration. This is the secret ingredient: allowing students to know just enough to feel comfortable making discoveries on their own.

Finally, encourage frequent testing. Every line of code added should automatically require a test run of the script.

Recap:

1. Demonstration of the finished product.
2. Section by section lecture of the concepts introduced.
3. Practice: give students time to try it out and complete any tasks.
4. Discuss.

You can take this further -- brevity here creates openings for each instructor to liberally modify and enhance the lesson. For example, you may allow students to swap code, pair, explain concepts, add new features, etc.


# Curriculum

This project tries to introduce new programmers to the python language by learning how to build very simple games. My approach is to provide tiny, small code snippets that introduce singular, isolated concepts. AFter a few lessons of these smaller snippets, students are invited to piece them together to create a complete game.

In the first lessons students learn to:
- Print text to the GUI
- Display images on the GUI (
- Move a square around on the GUI
- Add sound to the GUI
- Create logic for game play

These things combined allow them to create games that use keyboard or mouse inputs, display sprites, move them around and add sound effects to them.

It's important that learning to code is an interactive *and* interesting experience. By focusing on allowing students to visualize their code progress, I hope to invite them to dive deeper into programming concepts.

Typical programming introductions break down core concepts like data types and functions into separate and discreet lessons. I've tried do something different here.

The problem with breaking the core concepts down in such isolation is that nothing any creates with code will ever be broken down that way. Imagine a traditional western farm. Large swathes of land are cleared for a singular seed type to be planted all over it. A part of the field is left fallow while another is nourished. The farmer rotates through the parts of the fields each season to produce the maximum amount of that crop. The problem is there is it produces a singular crop, no variety and wastes many acres of land which become so depleted after each harvest that it's useless.

Now imagine the farming practices of Native American tradition. Several types of seeds, each complimentary to the next, are planted on the same area of land *together*. The harvest is usually smaller, but also provides a richer diet and, importantly, it doesn't exhaust the land -- farmers can continuously produce each season on the same land. It provides a more consistent source of food without all the waste.

My approach attempts to plant knowledge according to the latter: many concepts together that enrich one another and which are repeated in every lesson. This means the student gets constant exposure to the concepts and constantly uses them in their proper context.

# Instructor Notes

Collision:
```
self.rect.colliderect(target)
```