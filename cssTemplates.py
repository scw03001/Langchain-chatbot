css = '''
<style>
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    margin: 0;
    padding: 0;
}
.chat-container {
    max-width: 600px;
    margin: 20px auto;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
    overflow: hidden;
}
.chat-message {
    padding: 10px 20px;
    border-bottom: 1px solid #e0e0e0;
}
.chat-message:last-child {
    border-bottom: none;
}
.chat-message.user {
    background-color: #e7f3fe;
    text-align: left;
}
.chat-message.bot {
    background-color: #d1e7dd;
    text-align: right;
}
.chat-message .text {
    font-size: 16px;
    line-height: 1.4;
    color: black;
}
</style>
'''

bot = '''
<div class="chat-message bot">
    <div class="text"><strong>Bot: </strong> {{MSG}}</div>
</div>
'''

user = '''
<div class="chat-message user">
    <div class="text"><strong>User: </strong> {{MSG}}</div>
</div>
'''