class Contact:
    def __init__(self, name):
        self.name = name
        self.message_count = 0
        self.word_count = 0
        self.first_message_count = 0

    def avgWords(self):
        """
        Calculates the average words per message.
        """
        return float(self.word_count)/self.message_count

    def incrementMessages(self):
        """
        increment messages count by one.
        """
        self.message_count += 1

    def incrementFirstMessages(self):
        """
        increment first messages count by one.
        """
        self.first_message_count += 1

    def incrementWords(self, count):
        """
        Increment work count.

        :param int count: number of words to increment
        """
        self.word_count += count

    def getName(self):
        return self.name

    def getMessageCount(self):
        return self.message_count

    def getWordCount(self):
        return self.word_count

    def getFirstMessageCount(self):
        return self.first_message_count
