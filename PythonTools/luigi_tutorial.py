# http://mattiacinelli.com/tutorial-on-luigi-pipeline-part-1-introduction/

import luigi


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
        with self.output().open('w') as output_file:
            output_file.write('Hello, World ang Luigi! \n')

if __name__ == '__main__':
    luigi.run()
