# http://mattiacinelli.com/tutorial-on-luigi-pipeline-part-1-introduction/
#https://bionics.it/posts/luigi-tutorial#helloworld


import luigi
import time


class GenerateWords(luigi.Task):
    def output(self):
        return luigi.LocalTarget('luigi_files/words.txt')

    def run(self):
        words =['First', 'Second', 'Third']
        with self.output().open('w') as f:
            for word in words:
                f.write("{word} \n".format(word=word))


class CountLetters(luigi.Task):
    def requires(self):
        return GenerateWords()

    def output(self):
        return luigi.LocalTarget('local_files/letter_count.txt')

    def run(self):
        with self.input().open('r') as infile:
            words = infile.read().splitlines()
        with self.output().open('w') as outfile:
            for word in words:
                outfile.write('{word} : {count} \n').format(word = word, count="6")

class HelloWorld(luigi.Task):

    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget('luigi_files/hello_world.txt')

    def run(self):
        time.sleep(15)
        with self.output().open('w') as output_file:
            output_file.write('Hello, World ang Luigi and some othe people! \n')
        time.sleep(15)

class NameSubstituer(luigi.Task):

    name = luigi.Parameter()

    def requires(self):
        return HelloWorld()

    def output(self):
        return luigi.LocalTarget(self.input().path + '.name' + self.name)

    def run(self):
        time.sleep(15)
        with self.input().open('r') as infile, self.output().open('w') as outfile:
            text = infile.read()
            text = text.replace('World', self.name)
            outfile.write(text)
        time.sleep(15)

class TaskA(luigi.Task):
    def requires(self):
        return None
    def output(self):
        return luigi.LocalTarget('luigi_files/taska')
    def run(self):
        with self.output().open('w') as f:
            f.write('foo')

class TaskB(luigi.Task):
    def requires(self):
        return None
    def output(self):
        return luigi.LocalTarget('luigi_files/taskb')
    def run(self):
        with self.output().open('w') as f:
            f.write('bar')

class TaskC(luigi.Task):

    upstream_task = luigi.Parameter(default=TaskA())

    def requires(self):
        return upstream_task
    def output(self):
        return luigi.LocalTarget('luigi_files/taskc')
    def run(self):
        with self.input().open('r') as infile, self.output().open('w') as outfile:
            for line in infile:
                outfile.write(line)

class MyWorkflow(luigi.Task):
    def requires(self):
        return TaskC(upstream_task=TaskB())
    def output(self):
        return self.input()


if __name__ == '__main__':
    luigi.run()
