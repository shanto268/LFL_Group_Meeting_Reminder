# -*- coding: utf-8 -*-
"""
==================================================================
Program : LFL_Lab_Maintenance/start_
==================================================================
Summary:
    - will choose whose turn it is and send them an email
    - works with a daemon/cron controller for execution
"""
__author__ =  "Sadman Ahmed Shanto"
__date__ = "09/9/2022"
__email__ = "shanto@usc.edu"

import datetime
from HelperFunctions import *

if __name__ == "__main__":
    # weekday choice (day in advance)
    meeting_date = str(datetime.date.today() + datetime.timedelta(days=1))
    meeting_time = "2:30 PM"
    meeting_place = "SSC 319"

    # content of email
    content = "Tomorrow ({}) we have the LFL Lab Group Meeting at {} in {}. I just wanted to remind you that it is your turn to bring snacks 🥨.".format(meeting_date, meeting_time, meeting_place)

    """
    Logic:
    """
    # read emission file to see whose turn this week (i.e. at execution)
    recipient_name, recipient_email = extract_lab_maintainer()

    # create email for lab maintainer
    email_content = create_email(recipient_name, content=content)
    subjectLine = "LFL Meeting Snacks Reminder ({})".format(meeting_date)

    # send email to lab maintainer
    send_email(recipient_email, subjectLine, email_content)

    # update the record
    update_record()
