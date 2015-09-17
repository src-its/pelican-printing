import click

@click.command()
@click.option('--title', default=1, help='Number of greetings.')
@click.option('--name', prompt='title of author',
              help='The person to greet.')
def hello(title, name):

if __name__ == '__main__':
    hello()
