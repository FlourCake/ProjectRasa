function gpromote(mention) {
if (msg.body.toLowerCase().startsWith('!gadmintrue')) {
        let chat = await msg.getChat();
        if (chat.isGroup) {
            chat.promoteParticipants(mention);
            chat.sendSeen();
        } else {
            msg.reply('Command ini hanya dapat digunakan di grup.')
        }
    }
}

while (msg.mentionedIds.length > 0)
    setTimeout(gpromote, msg.mentionedIds.length * 5000, msg.mentionedIds.pop()) // Delaynya