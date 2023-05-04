<h1>Practice Exam</h1>

There was a practice exam on Thursday 20 April. For students who submitted a solution, personal feedback from the lecturers is available. For students who did not submit a solution, you can find the exam here in this folder to practice on your own.

<h3>List of files:</h3>

* 00_MBI04H_Programming2_PRACTICE_EXAM_coversheet.pdf
  * This is the coversheet which was available printed before the practice exam began. 
  * At the real exam in June (and 2nd exam chance in August/September), you will find a coversheet similar to this printed on the desk when you enter. You should read this before the exam begins.
* assignment.md
  * This file includes the description of the exercises you will need to solve for the (practice) exam.
* filesystem.py
  * This file is similar to the student.py files you work with during the exercises.
  * For the practice exam there is only one filesystem.py file you needed to fill in with your code.
  * On the real exam, there will likely be more than one, with different names.
* test_filesystem.py
  * __Important__: this is a set of superficial tests which *only* check that you have most of the necessary classes and members that we have asked for in the assignment. These tests *do not* check if your program's functionality is correct or complete.
  * On the real exam, you can write your own more complete tests to check your own work if this is helpful for you. You should practice solving exercises without relying on the output of comprehensive testing so you are well prepared for the exam.
  * To run these tests, open a terminal and run the following command: pytest test-filesystem.py
* tests-not-given-on-the-exam.py (found in practice-exam-tests folder)
  * These are the more comprehensive tests that will check the functionalities of your solution.
  * __Important__: tests such as these will __NOT__ be provided at the real exam in June or August/September. These are only intended for you to evaluate your practice solution.
  * Best practice: Attempt to solve the practice exam in its entirety, relying only on the assignment.md and test_filesystem.py, as well as your own insights into the problem. Only use the tests-not-given-on-the-exam.py at the end to review your solution and evaluate your work.
  * To use these more complete tests to check your practice exam, copy the tests-not-given-on-the-exam.py file to the folder where your filesystem.py file is. Then open a terminal and run the following command: pytest tests-not-given-on-the-exam.py