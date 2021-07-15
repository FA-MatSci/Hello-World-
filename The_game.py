#Copyrights Filip Ambroz

import sys
import random
import time


#Lets do the first 5 questions via **kwargs

class Question_class:
    def __init__(self, **kwargs):
        self.q1=kwargs['q1']
        self.q2=kwargs['q2']
        self.q3=kwargs['q3']
        self.q4=kwargs['q4']
        self.q5=kwargs['q5']
        
    print('Hello, World!\n\n' + 'Who Wants to Be a Millionaire?\n\n' + 'Before you start, may I ask you for some information? - ' 
    + 'We need that for lifelines!\n')   
    name1 = input('What is your name? >>>:')
    name2 = input('What is the name of your mother? >>>:')
    name3 = input('What is the name of your father? >>>:')
    name4 = input('What is the name of your best friend? >>>:')
            
    def qu1(self):
        return str('\nQuestion 1 \n\n ') + self.q1
    
    def qu2(self):
        return str('\nQuestion 2 \n\n') + self.q2
    
    def qu3(self):
        return str('\nQuestion 3 \n\n') + self.q3
    
    def qu4(self):
        return str('\nQuestion 4 \n\n') + self.q4
    
    def qu5(self):
        return str('\nQuestion 5 \n\n') + self.q5  
    
    

class Key_class:
    
    def qu1_keys(self):
        return str('a) Manchester \t\t\t\t') + str('b) London \n') + str('c) Liverpool \t\t\t\t') + str('d) Edinburgh \n')
    
    def qu2_keys(self):
        return str('a) 2 months \t\t\t\t') + str('b) 3 months \n') + str('c) 4 months \t\t\t\t') + str('d) 5 months \n')
    
    def qu3_keys(self):
        return str('a) vinum \t\t\t\t') + str('b) verba \n') + str('c) iuvat \t\t\t\t') + str('d) vici \n')
    
    def qu4_keys(self):
        return str('a) Jane Austen \t\t\t\t\t') + str('\tb) Mark Twain \n') + str('c) William Shakespeare \t\t\t\t') + str('d) Oscar Wilde \n')  
    
    def qu5_keys(self):
        return str('a) Jose Manuel Barroso \t\t\t\t') + str('b) Charles Michel \n') + str('c) Ursula von der Leyen \t\t\t') +str('d) David Sassoli \n')
    
    
    
class Input_class:    
     
     def input_qu1(self):
        self._a = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>:')
        return self._a          #this is internal attribute to the class Input_class
        
    
     def input_answer1(self):
        if self._a == 'London' or self._a == 'b' or self._a == 'b)' or self._a == 'london':
            return('\nLondon is the correct answer!!\n\n') + Correct_class.correct1()
        elif self._a == '1':
            return Lifeline1.q1lifeline1(self)
        elif self._a == '2':
            return Lifeline2.q1lifeline2(self)
        elif self._a == '3':
            return Lifeline3.q1lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 0 questions right (0/10 - miserable ' +
                     'performance) - Game Over!')
        
     def input_answer1lif(self):
        self._aa = input('Type your answer here >>>:')
        if self._aa == 'London' or self._aa == 'b' or self._aa == 'b)' or self._aa == 'london':
            return('\nLondon is the correct answer!!\n\n') + Correct_class.correct1()
        elif self._aa == '1':
            return Lifeline1.q1lifeline1(self)
        elif self._aa == '2':
            return Lifeline2.q1lifeline2(self)
        elif self._aa == '3':
            return Lifeline3.q1lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 0 questions right (0/10 - miserable ' +
                     'performance) - Game Over!')
    
     def input_qu2(self):
        self._b = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number - attention!'
                        +' For lifeline 3 type "3+") here >>>:')
        return self._b
    
     def input_answer2(self):
        if self._b == '3 months' or self._b == '3' or self._b == 'b' or self._b == 'b)':
            return('\n3 months is the correct answer!!\n\n') + Correct_class.correct2()
        elif self._b == '1':
            return Lifeline1.q2lifeline1(self)
        elif self._b == '2':
            return Lifeline2.q2lifeline2(self)
        elif self._b == '3+':
            return Lifeline3.q2lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 1 question right (1/10 - poor performance)' +
                     '- Game Over!')
            
     def input_answer2lif(self):
        self._bb = input('Type your answer here >>>:')
        if self._bb == '3 months' or self._bb == '3' or self._bb == 'b' or self._bb == 'b)':
            return ('\n3 months is the correct answer!!\n\n') + Correct_class.correct2()
        elif self._bb == '1':
            return Lifeline1.q2lifeline1(self)
        elif self._bb == '2':
            return Lifeline2.q2lifeline2(self)
        elif self._bb == '3+':
            return Lifeline3.q2lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 1 question right (1/10 - poor performance)' +
                     '- Game Over!')
     
     def input_qu3(self):
        self._c = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>:')
        return self._c
    
     def input_answer3(self):
        if self._c == 'vici' or self._c == 'd' or self._c == 'd)':
            return('\nvici is the correct answer!!\n\n') + Correct_class.correct3()
        elif self._c == '1':
            return Lifeline1.q3lifeline1(self)
        elif self._c == '2':
            return Lifeline2.q3lifeline2(self)
        elif self._c == '3':
            return Lifeline3.q3lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 2 questions right (2/10 - meager performance)' +
                     '- Game Over!')
            
     def input_answer3lif(self):
        self._cc = input('Type your answer here >>>:')
        if self._cc == 'vici' or self._cc == 'd' or self._cc == 'd)':
            return('\nvici is the correct answer!!\n\n') + Correct_class.correct3()
        elif self._cc == '1':
            return Lifeline1.q3lifeline1(self)
        elif self._cc == '2':
            return Lifeline2.q3lifeline2(self)
        elif self._cc == '3':
            return Lifeline3.q3lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 2 questions right (2/10 - meager performance)' +
                     '- Game Over!')
        
     def input_qu4(self):
            self._d = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>:')
            return self._d
        
     def input_answer4(self):
            if self._d == 'William Shakespeare' or self._d == 'Shakespeare' or self._d == 'c' or self._d == 'c)':
                return('\nWilliam Shakespeare is the correct answer!!\n\n') + Correct_class.correct4()
            elif self._d == '1':
                return Lifeline1.q4lifeline1(self)
            elif self._d == '2':
                return Lifeline2.q4lifeline2(self)
            elif self._d == '3':
                return Lifeline3.q4lifeline3(self)
            else:
                sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 3 questions right (3/10 - inferior performance)' +
                     '- Game Over!')
                
     def input_answer4lif(self):
        self._dd = input('Type your answer here >>>:')
        if self._dd == 'William Shakespeare' or self._dd == 'Shakespeare' or self._dd == 'c' or self._dd == 'c)':
            return('\nWilliam Shakespeare is the correct answer!!\n\n') + Correct_class.correct4()
        elif self._dd == '1':
            return Lifeline1.q4lifeline1(self)
        elif self._dd == '2':
            return Lifeline2.q4lifeline2(self)
        elif self._dd == '3':
            return Lifeline3.q4lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 3 questions right (3/10 - inferior performance)' +
                     '- Game Over!')
                
     def input_qu5(self):
        self._e = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>:')
        return self._e
    
     def input_answer5(self):
        if self._e == 'Ursula von der Leyen' or self._e == 'von der Leyen' or self._e == 'der Leyen' or self._e == 'der leyen' or self._e =='c' or self._e == 'c)':
            return('\nUrsula von der Leyen is the correct answer!!\n\n') + Correct_class.correct5()
        elif self._e == '1':
            return Lifeline1.q5lifeline1(self)
        elif self._e == '2':
            return Lifeline2.q5lifeline2(self)
        elif self._e == '3':
            return Lifeline3.q5lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 4 questions right (4/10 - insufficient performance)' +
                     '- Game Over!')
    
     def input_answer5lif(self):
        self._ee = input('Type your answer here >>>:')
        if self._ee == 'Ursula von der Leyen' or self._ee == 'von der Leyen' or self._ee == 'der Leyen' or self._ee == 'der leyen' or self._ee =='c' or self._ee == 'c)':
            return('\nUrsula von der Leyen is the correct answer!!\n\n') + Correct_class.correct5()
        elif self._ee == '1':
            return Lifeline1.q5lifeline1(self)
        elif self._ee == '2':
            return Lifeline2.q5lifeline2(self)
        elif self._ee == '3':
            return Lifeline3.q5lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You only answered 4 questions right (4/10 - insufficient performance)' +
                     '- Game Over!')
    
        
     def input_next_question(self):
        self.next = input('Type your answer here >>>:')
        if self.next == 'Next' or self.next == 'next':
            pass
        else:
            exit('Sorry to see you go! I hope you had a good time!')
            
    
        
class Correct_class:        #for right answers
        @classmethod
        def correct1(cls):
            return str('Type "Next" to proceed to Question 2 or "Quit" to close the game.\n')
        
        @classmethod
        def correct2(cls):
            return str('Type "Next" to proceed to Question 3 or "Quit" to close the game.\n')
        
        @classmethod
        def correct3(cls):
            return str('Type "Next" to proceed to Question 4 or "Quit" to close the game.\n')
        
        @classmethod
        def correct4(cls):
            return str('Type "Next" to proceed to Question 5 or "Quit" to close the game.\n')
        
        @classmethod
        def correct5(cls):
            return str('Type "Next" to proceed to Question 6 or "Quit" to close the game.\n')
   
   
        
        
#Lets do the next 2 questions on a different way
class Questions:
    def __init__(self):
        self.quest6 = '\nQuestion 6\n'
        self.quest7 = '\nQuestion 7\n'
    
    def question6(self):
        return str('What is the name of a very popular fantasy drama series created by David Benioff and D. B. Weiss?')
    
    def question7(self):
        return str('What year did the French Revolution begin?')
    
    
    def answer6(self):
        return str('a) Game of Thrones\t\t\t') + str('b) Lucifer\n') + str('c) Manifest\t\t\t\t\t') + str('d) The Witcher\n')
    
    def answer7(self):
        return str('a) 1786\t\t\t\t') + str('b) 1787\n') + str('c) 1788\t\t\t\t') + str('d) 1789\n')
    
 
    def input_q6(self):
        self._q6 = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>')
        if self._q6 == 'Game of Thrones' or self._q6 == 'a' or self._q6 == 'a)':
            self._answer6 = 'ok'
        elif self._q6 == '1':
            return Lifeline1.q6lifeline1(self)
        elif self._q6 == '2':
            return Lifeline2.q6lifeline2(self)
        elif self._q6 == '3':
            return Lifeline3.q6lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 5 questions right (5/10 - unsatisfactory ' +
                     'performance) ' + '- Game Over!')
    
    def input_q6lif(self):
        self._q6l = input('Type your answer here >>>')
        if self._q6l == 'Game of Thrones' or self._q6l == 'a' or self._q6l == 'a)':
            self._answer6 = 'ok'
        elif self._q6l == '1':
            return Lifeline1.q6lifeline1(self)
        elif self._q6l == '2':
            return Lifeline2.q6lifeline2(self)
        elif self._q6l == '3':
            return Lifeline3.q6lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 5 questions right (5/10 - unsatisfactory ' +
                     'performance) ' + '- Game Over!')
            
    def input_q7(self):
        self._q7 = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>')
        if self._q7 == '1789' or self._q7 == 'd' or self._q7 == 'd)':
            self._answer7 = 'ok'
        elif self._q7 == '1':
            return Lifeline1.q7lifeline1(self)
        elif self._q7 == '2':
            return Lifeline2.q7lifeline2(self)
        elif self._q7 == '3':
            return Lifeline3.q7lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 6 questions right (6/10 - inadequate ' +
                     'performance) ' + '- Game Over!')
            
    def input_q7lif(self):
        self._q7l = input('Type your answer here >>>')
        if self._q7l == '1789' or self._q7l == 'd' or self._q7l == 'd)':
            self._answer7 = 'ok'
        elif self._q7l == '1':
            return Lifeline1.q7lifeline1(self)
        elif self._q7l == '2':
            return Lifeline2.q7lifeline2(self)
        elif self._q7l == '3':
            return Lifeline3.q7lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 6 questions right (6/10 - inadequate ' +
                     'performance) ' + '- Game Over!')
    
       
    def correct6(self):
        if hasattr(self, '_answer6'):
            return str('\nGame of Thrones is the correct answer!!') + str('\n\nType "Next" to proceed to Question 7' +
            ' or "Quit" to close the game.\n')
        else:
            pass
    
    def correct7(self):
        if hasattr(self, '_answer7'):
            return str('\n1789 is the correct answer!!') + str('\n\nType "Next" to proceed to Question 7' +
            ' or "Quit" to close the game.\n')                                                               
    
    
    def next_one6(self):
        self.next6 = input('Type your answer here >>>')
        if self.next6 == 'Next' or self.next6 == 'next':
            return self.quest7
        else:
            sys.exit('Sorry to see you go! I hope you had a good time!')
            
    def next_one7(self):
        self.next7 = input('Type your answer here >>>')
        if self.next7 == 'Next' or self.next7 == 'next':
            return str('')
        else:
            sys.exit('Sorry to see you go! I hope you had a good time!')
 
    
#Lets do the next question via composition
class Composite:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
    
    
class Question8:
    
    def __str__(self):
        return '\nQuestion 8\n' + '\nWho among the listed researchers is considered a pioneer in the field of perovskite solar cells?'


class Answers:  
    
    def __str__(self):
        return 'a) Omar Yaghi\t\t\t\t\t' + 'b) John Goodenough\n' + 'c) Akira Fujishima\t\t\t\t' + 'd) Henry Snaith'
    
    def input(self):
        self.input8 = input('\nType your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>')
        if self.input8 == 'Henry Snaith' or self.input8 == 'Snaith' or self.input8 == 'd' or self.input8 == 'd)':
            print('\nHenry Snaith is the correct answer!!' + '\n\nType "Next" to proceed to Question 7 ' + 'or "Quit" to close the game.\n')
        elif self.input8 == '1':
            return Lifeline1.q8lifeline1(self)
        elif self.input8 == '2':
            return Lifeline2.q8lifeline2(self)
        elif self.input8 == '3':
            return Lifeline3.q8lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 7 questions right (7/10 - acceptable performance)' +
                     ' - Game Over!')
        
    def inputlif(self):
        self.input8l = input('\nType your answer here >>>')
        if self.input8l == 'Henry Snaith' or self.input8l == 'Snaith' or self.input8l == 'd' or self.input8l == 'd)':
            print('\nHenry Snaith is the correct answer!!' + '\n\nType "Next" to proceed to Question 7 ' + 'or "Quit" to close the game.\n')
        elif self.input8l == '1':
            return Lifeline1.q8lifeline1(self)
        elif self.input8l == '2':
            return Lifeline2.q8lifeline2(self)
        elif self.input8l == '3':
            return Lifeline3.q8lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 7 questions right (7/10 - acceptable performance)' +
                     ' - Game Over!')
        
    def proceed(self):
        self.proceed = input('Type your answer here >>>')
        if self.proceed == 'Next' or self.proceed == 'next':
            pass
        else:
            sys.exit('\nSorry to see you go! I hope you had a good time!')


#Lets do the next question via inheritance
class Question9:
    
    question = '\nQuestion 9\n'     #class attribute
        
    def question9(self):
        return 'Which two software engineers created a cryptocurrency called Dogecoin?'
    
    def answer9(self):
        return 'a) Billy Markus and Jackson Palmer' + '\t\t\tb) Satoshi Nakamoto and Hal Finney' + '\nc) Nick Szabo and Craig Wright\t\t\t\t' + 'd) Vitalik Buterin and Gavin Wood\n'
    
class Input9(Question9):
    def inp9(self):
        self.inp9 = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>:')
        if self.inp9 == 'Billy Markus and Jackson Palmer' or self.inp9 == 'Markus and Palmer' or self.inp9 == 'a' or self.inp9 == 'a)':
            return '\nBilly Markus and Jackson Palmer is the correct answer!!\n\n' + 'Type "Next" to proceed to the final Question' + ' or "Quit" to close the game.\n'
        elif self.inp9 == '1':
            return Lifeline1.q9lifeline1(self)
        elif self.inp9 == '2':
            return Lifeline2.q9lifeline2(self)
        elif self.inp9 == '3':
            return Lifeline3.q9lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 8 questions right (8/10 - excellent performance)' + ' - Game Over!')
    
    def inp9lif(self):
        self.inp9l = input('Type your answer here >>>:')
        if self.inp9l == 'Billy Markus and Jackson Palmer' or self.inp9l == 'Markus and Palmer' or self.inp9l == 'a' or self.inp9l == 'a)':
            return '\nBilly Markus and Jackson Palmer is the correct answer!!\n\n' + 'Type "Next" to proceed to the final Question' + ' or "Quit" to close the game.\n'
        elif self.inp9l == '1':
            return Lifeline1.q9lifeline1(self)
        elif self.inp9l == '2':
            return Lifeline2.q9lifeline2(self)
        elif self.inp9l == '3':
            return Lifeline3.q9lifeline3(self)
        else:
            sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 8 questions right (8/10 - excellent performance)' + ' - Game Over!')
    

    def proceed9(self):
        self.proceed9 = input('Type your answer here >>>')
        if self.proceed9 == 'Next' or self.proceed9 == 'next':
            return ' '
        else:
            sys.exit('Sorry to see you go! I hope you had a good time!')
        
        
#Lets do the final question via magic methods
class Attr:
    def __init__(self, name=None):
        self.name = name
        
    def __getattribute__(self, item):
        object.__getattribute__(self, item)
        return '\nJustin I is the correct answer!!\n\n' + 'YOU JUST WON A MILLION $$$$$!!' + ' You answered 10 questions right (10/10 - outstanding performance)!!' + '\n\t\t\t\t\t\t\t\tWELL DONE AND CONGRATULATIONS!!'
    
    def __getattr__(self, item):
        return sys.exit('\nYour answer is wrong!!\n\n' + 'You answered 9 questions right (9/10 - phenomenal performance)' + ' - Game Over!')

class Question10:       #in attr class you can't have other methods
    
    def quest10(self):
        return 'Who was the first Byzantine emperor of the Justinian dynasty (518 - 602)?'
    
    def answ10(self):
        return 'a) Justinian I\t\t\t\t\t' + 'b) Justin I\n' + 'c) Anastasius I\t\t\t\t\t' + 'd) Constantine I\n'
    
    def inp10lif(self):
        inpl = input('Type your answer here >>>')
        if inpl == 'b' or inpl == 'b)' or inpl == 'Justin I' or inpl == 'justin I':
            print('\nJustin I is the correct answer!!\n\n' + 'YOU JUST WON A MILLION $$$$$!!' + ' You answered 10 questions right (10/10 - outstanding performance)!!' + '\n\t\t\t\t\t\t\t\tWELL DONE AND CONGRATULATIONS!!')
        elif inpl == '1':
            return Lifeline1.q10lifeline1(self)
        elif inpl == '2':
            return Lifeline2.q10lifeline2(self)
        elif inpl == '3':
            return Lifeline3.q10lifeline3(self)
        else:
            print('\nYour answer is wrong!!\n\n' + 'You answered 9 questions right (9/10 - phenomenal performance)' + ' - Game Over!')
    

class Lifeline1:

    called = False
    
    def q1lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) / \t\t\t\t' + 'b) London \n' + 'c) / \t\t\t\t' + 'd) Edinburgh \n')
        time.sleep(1.5)
        return Input_class.input_answer1lif(self)
        
        
    def q2lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) / \t\t\t\t' + 'b) 3 months \n' + 'c) 4 months \t\t' + 'd) / \n')
        time.sleep(1.5)
        return Input_class.input_answer2lif(self)
    
        
    def q3lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) vinum \t\t\t' + 'b) / \n' + 'c) / \t\t\t\t' + 'd) vici \n')
        time.sleep(1.5)
        return Input_class.input_answer3lif(self)
        
    def q4lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) Jane Austen \t\t\t\t\t' + '\tb) / \n' + 'c) William Shakespeare \t\t\t\t' + 'd) / \n')
        time.sleep(1.5)
        return Input_class.input_answer4lif(self)
        
    def q5lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) / \t\t\t\t\t\t\t\t' + 'b) Charles Michel \n' + 'c) Ursula von der Leyen \t\t\t' + 'd) / \n')
        time.sleep(1.5)
        return Input_class.input_answer5lif(self)
        
    def q6lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) Game of Thrones\t\t\t' + 'b) Lucifer\n' + 'c) /\t\t\t\t\t\t' + 'd) /\n')
        time.sleep(1.5)
        return Questions.input_q6lif(self)
    
    def q7lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) /\t\t\t\t' + 'b) 1787\n' + 'c) /\t\t\t\t' + 'd) 1789\n')
        time.sleep(1.5)
        return Questions.input_q7lif(self)
    
    def q8lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) /\t\t\t\t' + 'b) John Goodenough\n' + 'c) /\t\t\t\t' + 'd) Henry Snaith')
        time.sleep(1.5)
        return Answers.inputlif(self)
        
    def q9lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) Billy Markus and Jackson Palmer' + '\t\t\tb) /' + '\nc) Nick Szabo and Craig Wright\t\t\t\t' + 'd) /\n')
        time.sleep(1.5)
        return Input9.inp9lif(self)
    
    def q10lifeline1(self):
        if Lifeline1.called:
            raise Exception("Lifeline 1 may only be used once")
        Lifeline1.called = True
        print('\nLifeline 1 (50:50) called!\n\n' \
        + 'a) Justinian I\t\t\t' + 'b) Justin I\n' + 'c) /\t\t\t\t\t' + 'd) /\n')
        time.sleep(1.5)
        return Question10.inp10lif(self)

 
class Lifeline2:
    
    called = False
    
    def q1lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        a = random.randrange(1,5,1)
        b = random.randrange(70,80,1)
        c = random.randrange(10,13,1)
        d = random.randrange(1,2,1)
        e = 100
        f = e-a-b-c-d
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}% \t\t\t\t'.format(a) + 'b) {}% \n'.format(b) + 'c) {}% \t\t\t\t'.format(d) + 'd) {}% \n'.format(c+f))
        time.sleep(1.5)
        return Input_class.input_answer1lif(self)
    

    def q2lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(20,23,1)
        h = random.randrange(45,60,1)
        i = random.randrange(10,14,1)
        j = random.randrange(1,3,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}% \t\t\t\t'.format(g) + 'b) {}% \n'.format(h) + 'c) {}% \t\t\t\t'.format(i+l) + 'd) {}% \n'.format(j))
        time.sleep(1.5)
        return Input_class.input_answer2lif(self)
    
    
    def q3lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(10,20,1)
        h = random.randrange(8,10,1)
        i = random.randrange(2,5,1)
        j = random.randrange(55,65,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}% \t\t\t\t'.format(g) + 'b) {}% \n'.format(h+l) + 'c) {}% \t\t\t\t'.format(i) + 'd) {}% \n'.format(j))
        time.sleep(1.5)
        return Input_class.input_answer3lif(self)
    
    def q4lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(20,29,1)
        h = random.randrange(23,29,1)
        i = random.randrange(30,39,1)
        j = random.randrange(1,3,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}% \t\t\t'.format(g) + '\tb) {}% \n'.format(h) + 'c) {}% \t\t\t\t'.format(i) + 'd) {}% \n'.format(j+l))
        time.sleep(1.5)
        return Input_class.input_answer4lif(self)
    
    def q5lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(20,29,1)
        h = random.randrange(23,30,1)
        i = random.randrange(29,38,1)
        j = random.randrange(1,3,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}% \t\t\t'.format(g) + 'b) {}% \n'.format(h) + 'c) {}% \t\t\t'.format(i) + 'd) {}% \n'.format(j+l))
        time.sleep(1.5)
        return Input_class.input_answer5lif(self)
    
    def q6lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(30,35,1)
        h = random.randrange(23,30,1)
        i = random.randrange(20,25,1)
        j = random.randrange(5,10,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}%\t\t\t'.format(g+l) + 'b) {}%\n'.format(h) + 'c) {}%\t\t\t'.format(i) + 'd) {}%\n'.format(j))
        time.sleep(1.5)
        return Questions.input_q6lif(self)
    
    def q7lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(5,10,1)
        h = random.randrange(23,30,1)
        i = random.randrange(20,30,1)
        j = random.randrange(25,30,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}%\t\t\t\t'.format(g+l) + 'b) {}%\n'.format(h) + 'c) {}%\t\t\t\t'.format(i) + 'd) {}%\n'.format(j))
        time.sleep(1.5)
        return Questions.input_q7lif(self)
    
    def q8lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(5,10,1)
        h = random.randrange(23,25,1)
        i = random.randrange(20,30,1)
        j = random.randrange(25,35,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}%\t\t\t\t'.format(g+l) + 'b) {}%\n'.format(h) + 'c) {}%\t\t\t\t'.format(i) + 'd) {}%'.format(j))
        time.sleep(1.5)
        return Answers.inputlif(self)
    
    def q9lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(20,25,1)
        h = random.randrange(20,25,1)
        i = random.randrange(20,25,1)
        j = random.randrange(20,25,1)
        k = 100
        l = (k-g-h-i-j)
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}%'.format(g) + '\t\t\tb) {}%'.format(h+l) + '\nc) {}%\t\t\t'.format(i) + 'd) {}%\n'.format(j))
        time.sleep(1.5)
        return Input9.inp9lif(self)
    
    def q10lifeline2(self):
        if Lifeline2.called:
            raise Exception("Lifeline 2 may only be used once")
        Lifeline2.called = True
        g = random.randrange(15,25,1)
        h = random.randrange(15,25,1)
        i = random.randrange(15,25,1)
        j = random.randrange(15,25,1)
        k = 100
        l = k-g-h-i-j
        print('\nLifeline 2 - Ask The Audience - called!\n\n' \
        + 'a) {}% \t\t\t\t\t'.format(g) + 'b) {}% \n'.format(h) + 'c) {}% \t\t\t\t\t'.format(i) + 'd) {}% \n'.format(j+l))
        time.sleep(1.5)
        return Question10.inp10lif(self)
   
   
class Lifeline3:
    
    called = False
    
    def q1lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        a = '{}: Hello Father, how are you?\n\n'.format(Question_class.name1) + '{}: Good afternoon! Who is calling?\n\n'.format(Question_class.name3)\
        + "{}: It is me, {}! I need your help with the 1st question!\n\n".format(Question_class.name1, Question_class.name1) \
        + '{}: With the first question?!?! You must be joking!\n\n'.format(Question_class.name3) \
        + '{}: Unfortunately, I am not! What is the capital city of England?\n\n'.format(Question_class.name1) \
        + '{}: Shameful that you must ask for that! It is London!!\n\n'.format(Question_class.name3)
        for q1l3 in a:
            sys.stdout.write(q1l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Input_class.input_answer1lif(self)
    
    def q2lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        b = '{}: Hi Mother, it is me {}!\n\n'.format(Question_class.name1, Question_class.name1) + '{}: {}! Where are you? Did you make it to the game?\n\n'.format(Question_class.name2, Question_class.name1) \
        + '{}: Yes, I did! However, I am stuck at the second question!\n\n'.format(Question_class.name1) \
        + '{}: You need my help at the second question?? That is pathetic!\n\n'.format(Question_class.name2) \
        + '{}: How many months are in summer season?\n\n'.format(Question_class.name1) + "{}: Don't know whether I should laugh or cry! There are 3!!\n\n".format(Question_class.name2)
        for q2l3 in b:
            sys.stdout.write(q2l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Input_class.input_answer2lif(self)
    
    def q3lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        c = '{}: Hi {}! It is me, {}!\n\n'.format(Question_class.name1, Question_class.name4, Question_class.name1) \
        + '{}: {}!! How is it going?\n\n'.format(Question_class.name4, Question_class.name1) + '{}: Not too bad! I need your help. I made it to the game!\n\n'.format(Question_class.name1) \
        + '{}: Wow! Amazing! I will try to help!\n\n'.format(Question_class.name4) + '{}: veni, vidi, what is next?\n\n'.format(Question_class.name1) \
        + '{}: As Julius Caesar used to say: veni, vidi, vici!\n\n'.format(Question_class.name4)
        for q3l3 in c:
            sys.stdout.write(q3l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Input_class.input_answer3lif(self)
   
    def q4lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n') 
        d = '{}: Hi Father! I am at the game and don\'t know an answer to the question!\n\n'.format(Question_class.name1) \
        + '{}: How far have you come?\n\n'.format(Question_class.name3) + '{}: I am at the fourth question.\n\n'.format(Question_class.name1) \
        + '{}: A bit early to use a lifeline!\n\n'.format(Question_class.name3) + '{}: Who wrote Hamlet and Macbeth?\n\n'.format(Question_class.name1) \
        + '{}: I assume that you would have known that! It\'s Shakespeare!\n\n'.format(Question_class.name3) + '{}: Cheers!\n\n'.format(Question_class.name1)
        for q4l3 in d:
            sys.stdout.write(q4l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Input_class.input_answer4lif(self)
          
    def q5lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        e = '{}: Am I speaking to {}?\n\n'.format(Question_class.name1, Question_class.name4) + '{}: Yes {}, {} speaking!\n\n'.format(Question_class.name4, Question_class.name1, Question_class.name4) \
        + '{}: I need help with the fifth question at Who Wants to be a Millionaire!\n\n'.format(Question_class.name1) \
        + '{}: Sounds good! Let\'s see what I can do.\n\n'.format(Question_class.name4) \
        + '{}: The current president of the European Commission? der Leyen or Michel?\n\n'.format(Question_class.name1) \
        + '{}: Mhmmm, I think it is Ursula von der Leyen.\n\n'.format(Question_class.name4)
        for q5l3 in e:
            sys.stdout.write(q5l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Input_class.input_answer5lif(self)
    
    def q6lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        f = '{}: Hello {}, I think that you could know the question that I am struggling with.\n\n'.format(Question_class.name1, Question_class.name4) \
        + '{}: Who is calling?\n\n'.format(Question_class.name4) + '{}: It is me, {}!\n\n'.format(Question_class.name1, Question_class.name1) \
        + '{}: Hi {}! Sounds good! Let me know what you need!\n\n'.format(Question_class.name4, Question_class.name1) \
        + '{}: Do you know about that famous series that was created by Weiss and Benioff?\n\n'.format(Question_class.name1) \
        + '{}: Mhmm, do you mean Lucifer?\n\n'.format(Question_class.name4) \
        + '{}: I think that is wrong. I believe it is the Game of Thrones?\n\n'.format(Question_class.name1) \
        + '{}: Yes, it might be!\n\n'.format(Question_class.name4)
        for q6l3 in f:
            sys.stdout.write(q6l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Questions.input_q6lif(self)
    
    def q7lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        g = '{}: Mom, {} here!\n\n'.format(Question_class.name1, Question_class.name1) + '{}: {}! Nice to hear from you!\n\n'.format(Question_class.name2, Question_class.name1) \
        + '{}: Since you know history, you might be helpful with this question!\n\n'.format(Question_class.name1) \
        + '{}: Ok.\n\n'.format(Question_class.name2) + '{}: French Revolution! What year did it start?\n\n'.format(Question_class.name1) \
        + '{}: That is a tough one! I think one of the two: 1787 or 1789!\n\n'.format(Question_class.name2)
        for q7l3 in g:
            sys.stdout.write(q7l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Questions.input_q7lif(self)
    
    def q8lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        h = '{}: Hey mate! It is me, {}!\n\n'.format(Question_class.name1, Question_class.name1) + '{}: {}!! Are you participating in the game?\n\n'.format(Question_class.name4, Question_class.name1) \
        + '{}: That is correct! Who started with perovskite solar cells? I think it is one of Goodenough, Yaghi or Snaith?\n\n'.format(Question_class.name1) \
        + '{}: Sorry, but I have no idea!! I know it has started in Oxford though!\n\n'.format(Question_class.name4)
        for q8l3 in h:
            sys.stdout.write(q8l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Answers.inputlif(self)
    
    
    def q9lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n') 
        j = '{}: Hi Father! I need your help! I am at the ninth question!\n\n'.format(Question_class.name1) \
        + '{}: Amazing! You will be a millionaire!! I am proud of you!\n\n'.format(Question_class.name3) \
        + '{}: Who created Dogecoin?\n\n'.format(Question_class.name1) + '{}: Dogecoin to the moon! Elon Musk\'s favourite crypto!\n\n'.format(Question_class.name3) \
        + '{}: Was it Nakamoto?\n\n'.format(Question_class.name1) + '{}: Nah, that was Bitcoin!\n\n'.format(Question_class.name3) + '{}: Then who was it?\n\n'.format(Question_class.name1) \
        + '{}: Mhm, I know there were two guys but don\'t know which ones! Sorry!\n\n'.format(Question_class.name3)
        for q9l3 in j:
            sys.stdout.write(q9l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Input9.inp9lif(self)
    
    def q10lifeline3(self):
        if Lifeline3.called:
            raise Exception("Lifeline 3 may only be used once")
        Lifeline3.called = True
        print('\nLifeline 3 (call) called!\n\n')
        k = '{}: Good evening mother! I am at the last question!!\n\n'.format(Question_class.name1) \
        + '{}: That\'s insane! How did you manage to come that far?\n\n'.format(Question_class.name2) \
        + '{}: I struggle with the last one! It\'s ridiculous!\n\n'.format(Question_class.name1) \
        + '{}: I can imagine!\n\n'.format(Question_class.name2) + '{}: The first Byzantine emperor of the Justinian dynasty?\n\n'.format(Question_class.name1) \
        + '{}: I have no idea! Good luck!\n\n'.format(Question_class.name2)
        for q10l3 in k:
            sys.stdout.write(q10l3)
            sys.stdout.flush()
            time.sleep(0.2)
        return Question10.inp10lif(self)

        
def main():
    object1 = Question_class(q1='What is the capital city of England?',  q2='How many months are in summer ' +
                             'season (Northern Hemisphere)?', q3='Continue the following Latin phrase: veni, vidi,', 
                             q4='Who wrote the famous plays Hamlet and Macbeth?', q5='Who is the current President ' +
                             'of the European Commission?')
    
    object2 = Key_class()
    object3 = Input_class()
    object4 = Correct_class()
    object5 = Questions()
    
    object6 = Question8()
    object7 = Answers()
    object8 = Composite(object6, object7)
    
    object9 = Input9()
    
    object10 = Attr()
    object11 = Question10()
    
    object12 = Lifeline1()
    object13 = Lifeline2()
    object14 = Lifeline3()
    
    print(object1.qu1())
    print(object2.qu1_keys())
    object3.input_qu1()
    print(object3.input_answer1())
    object3.input_next_question()
    print(object1.qu2())            #you can't call **kwargs (e.g. self.q2 in def qu2()) inside the method
    print(object2.qu2_keys())
    object3.input_qu2()
    print(object3.input_answer2())
    object3.input_next_question()
    print(object1.qu3())
    print(object2.qu3_keys())
    object3.input_qu3()
    print(object3.input_answer3())
    object3.input_next_question()
    print(object1.qu4())
    print(object2.qu4_keys())
    object3.input_qu4()
    print(object3.input_answer4())
    object3.input_next_question()
    print(object1.qu5())
    print(object2.qu5_keys())
    object3.input_qu5()
    print(object3.input_answer5())
    object3.input_next_question()
    
    print(object5.quest6)
    print(object5.question6())
    print(object5.answer6())
    object5.input_q6()
    print(object5.correct6())
    print(object5.next_one6())
    print(object5.question7())
    print(object5.answer7())
    object5.input_q7()
    print(object5.correct7())
    print(object5.next_one7())
    
    print(object8.question)
    print(object8.answers)
    object7.input()
    object7.proceed()
    
    print(getattr(object9, 'question'))
    print(object9.question9())
    print(object9.answer9())
    print(object9.inp9())
    print(object9.proceed9())
    
    print('\nQuestion 10\n')
    print(object11.quest10())
    print(object11.answ10())

    inp = input('Type your answer (for lifelines 1 (50:50), 2 (ask the audience) or 3 (call) type the number) here >>>')
    if inp == 'b' or inp == 'b)' or inp == 'Justin I' or inp == 'justin I':
        print(object10.name)
    elif inp == '1':
        return object12.q10lifeline1()
    elif inp == '2':
        return object13.q10lifeline2()
    elif inp == '3':
        return object14.q10lifeline3()
    else:
        print(object10.nothing)
    
    
    
    
    
    
    


if __name__ == '__main__':
    main()    

