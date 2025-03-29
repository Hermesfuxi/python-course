import os

class ChatBot:
    def __init__(self, name):
        self.name = name
        self.mood = '😀'
        self.message_list = []

        file_name = f'{self.name}_chat.log'
        file_path = rf'.\{file_name}'
        if os.path.exists(file_path):
            with open(rf'.\{file_name}', 'r', encoding='utf-8') as f:
                for line in f:
                    self.message_list.append(line.strip())

    def reply(self, message):
        self.message_list.append(f'用户：{message}')
        return_str = ''

        if "开心" in message:
            self.mood = '😂'
            return_str = '我也为您感到高兴！'
        elif '难过' in message:
            self.mood = '😔'
            return_str = '希望我能帮到您...'
        else:
            self.mood = '🤖'
            return_str = '收到您的消息，正在处理中~'

        return_str = f'{self.name}: {self.mood} {return_str}'
        self.message_list.append(return_str)
        print(return_str)
        # return return_str

    def show_history(self, message_count=3):
        len_lst = len(self.message_list)
        start_index = 0 if (start_index := len_lst - message_count) < 0 else start_index
        for i in (self.message_list[start_index::]):
            print(i)

    def __str__(self):
        return f'AI客服{self.name} | 已处理对话：{len(self.message_list)}条'

    def __del__(self):
        file_name = f'{self.name}_chat.log'
        with open(rf'.\{file_name}', 'a') as f:
            for line in self.message_list:
                f.write(line+'\n')
        print('对话记录已加密保存到【小冰_chat.log】')


xiaoyu = ChatBot('小雨')
xiaoyu.show_history()
print(xiaoyu)
xiaoyu.reply('我很难过')
print(xiaoyu)
xiaoyu.reply('我很开心')
xiaoyu.reply('你可以帮我吗')
print(xiaoyu)
xiaoyu.show_history(5)
del xiaoyu