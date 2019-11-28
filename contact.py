class Contact:
    def __init__(self, name):
        self.name = name
        self.message_count = 0
        self.word_count = 0
        self.first_message_count = 0
        self.hourly_message_count = [0] * 24
        self.daily_message_count = [0] * 7
        self.monthly_message_count = [0] * 12

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

    def incrementTimeCount(self, time):
        """
        Increment the messages time counter by 1.

        :param time_struct time: Time stored in a time_struct
        """
        self.hourly_message_count[time.tm_hour] += 1
        self.daily_message_count[time.tm_wday] += 1
        self.monthly_message_count[time.tm_mon-1] += 1

    def getName(self):
        return self.name

    def getMessageCount(self):
        return self.message_count

    def getWordCount(self):
        return self.word_count

    def getFirstMessageCount(self):
        return self.first_message_count

    def getHourlyMessageCount(self):
        return self.hourly_message_count

    def getDailyMessageCount(self):
        return self.daily_message_count

    def getMonthlyMessageCount(self):
        return self.monthly_message_count
