from jira import JIRA

jiraOptions = {'server': "https://opusonline-test.atlassian.net"} 
  
jira = JIRA(options=jiraOptions, basic_auth=( 
    "henry.naptal@opusonline.co", "ATATT3xFfGF0TSJWSon0VQYwzN2MwHzk-A-bx6telsJlM0nbd3BQhHFDhW4lV4AiGmH0Xa09gyF5tGeZBc8vMzc_6IitUOWbIj3WuisFTHBI3HhHDPT8MBXH6ojy7G117wj-DH9Eh6OnuZiAK9rZ_she9_FUdiTpGPgURbfl9F_7O33VpNiJIh8=E14E72A1")) 
  
singleIssue = jira.issue('KAN-1') 
print('Ticket key: {},\r\nTicket name: {},\r\nTicket reporter: {}'.format(singleIssue.key, 
                         singleIssue.fields.summary, 
                         singleIssue.fields.reporter.displayName)) 