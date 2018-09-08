# smtp-firewall
A python project that aims to proxy SMTP traffic and drop emails based on a ruleset.

### Why?
Intended to give developers and application admins increased control of how their application sends an email. Particularly useful during development of applications or testing scenarios where you may want some test users to receive email, but not everyone. 

Some organizations provide an 'internal only' smtp server that you can use to limit exposure should emails get sent out automatically. This still doesn't prevent you from accidently spamming the rest of your team, or worse, C-level executives.

### Planned Features
- Server/sender specific ruleset - Allows you to set custom rules based on which application server is trying to send the email
- whitelisted emails only - Only allow emails to be sent if the email matches a regex or individual email in a list
- blacklisted - explicity block emails from being sent to a recipient(s)
- rule behaviors - if a message fails a rule and contains a recipient that should not be receiving email, the message can be DROPPED, FILTERED(recipient removed)
