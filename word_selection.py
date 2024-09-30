import random

# Load the word list once at the beginning of the script
WORDS = [
    'python', 'hangman', 'challenge', 'programming', 'developer',
    'algorithm', 'function', 'variable', 'syntax', 'exception',
    'iteration', 'recursion', 'compiler', 'interpreter', 'debugging',
    'inheritance', 'polymorphism', 'encapsulation', 'abstraction',
    'lambda', 'database', 'framework', 'library', 'module',
    'package', 'virtualization', 'encryption', 'compression',
    'deployment', 'container', 'orchestration', 'binary', 'cache',
    'optimization', 'parallelization', 'threading', 'asynchronous',
    'synchronization', 'networking', 'protocol', 'architecture',
    'interface', 'middleware', 'scalability', 'firewall', 'kernel',
    'router', 'switch', 'gateway', 'bandwidth', 'latency'
]

def get_random_word():
    """
    This function selects and returns a random word from the predefined list of words.
    It uses the random.choice method to pick a word from the WORDS list.
    """
    return random.choice(WORDS).upper()
