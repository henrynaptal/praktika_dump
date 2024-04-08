from jira import JIRA

jiraOptions = {'server': "https://opusonline-test.atlassian.net"} 
  
jira = JIRA(options=jiraOptions, basic_auth=( 
    "henry.naptal@opusonline.co", "API_TOKEN")) 
  
singleIssue = jira.issue('KAN-1') 
print('Ticket key: {},\r\nTicket name: {},\r\nTicket reporter: {}'.format(singleIssue.key, 
                         singleIssue.fields.summary, 
                         singleIssue.fields.reporter.displayName)) 