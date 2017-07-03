from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
from employees import Employees
from employers import Employers
import config

import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                              level=logging.INFO)


logger = logging.getLogger(__name__)
DECISION,WORKER,EMPLOYER,WORKERS,EMPLOYERS,ENROLL,PHONE,EMAIL,SPECIALITY,DAILYRATE,JOBS,POSTJOBS,CONTACT = range(13);

user_details = dict();

def echo(bot,update):
    update.message.reply_text(" {} you said {} ".format(update.message.from_user['username'],update.message.text));

def start(bot, update):
    # build a keyboard
    reply_keyboard = [['Job_Seeker', 'Employer','Cancel']]
    #capture user details
    name = update.message.from_user;
    chat_id = update.message.chat_id;
    # store details in a dictionary
    user_details['name'] = name;
    user_details['chat_id']= chat_id;

    update.message.reply_text(
        'Hi! Clients ? I am a bot and I connect Job Seekers with\
         Employers. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a Job Seeker or an Employer?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

    return DECISION;

def decision(bot,update):
    user_details['user_type'] = update.message.text;
    worker_keyboard = [['Enroll','Available Jobs','Employers','Cancel']];
    comp_keyboard =[['Enroll','Post Jobs','Workers','Cancel']];
    choice = update.message.text;

    if choice == 'Job_Seeker':
        emp = Employees();
        update.message.reply_text('Hi,make your choice \n',
        reply_markup=ReplyKeyboardMarkup(worker_keyboard, one_time_keyboard = True))
        return WORKER;
    elif choice == 'Employer':
        update.message.reply_text('Hi,kindly enroll',
        reply_markup=ReplyKeyboardMarkup(comp_keyboard, one_time_keyboard = True))
        return EMPLOYER;
    else:
        return ConversationHandler.END;


def worker(bot,update):
    choice = update.message.text;
    if choice == 'Enroll':
        return PHONE;
    elif choice == 'Available Jobs':
        return JOBS;
    elif choice == 'Employers':
        return EMPLOYERS;
    else:
        return DECISION;

def employer_co(bot,update):
    choice = update.message.text;
    if choice == 'Enroll':
        return PHONE;
    elif choice == 'Post Jobs':
        return POSTJOBS;
    elif choice == 'Workers':
        return WORKERS;
    else:
        return DECISION;

def get_phone_no(bot,update):
    echo(bot,update);
    update.message.reply_text(
    'Kindly let us know your phone number'
    );
    return EMAIL;

def get_email(bot,update):
    echo(bot,update);
    user_details['email'] = update.message.text;
    if user_details['user_type'] == 'Employer':
        update.message.reply_text(
        ' Please let us know your career'
        );
        return SPECIALITY;
    else:
        update.message.reply_text(
        ' Please let us know your person contact.'
        );
        return CONTACT;

def skip_email(bot,update):
    echo(bot,update);

def get_worker_speciality(bot,update):
    echo(bot,update);
    user_details['speciality'] = update.message.text;
    update.message.reply_text(
    'Kindly let us know your daily rate'
    );
    return DAILYRATE;

def get_worker_daily_rate(bot,update):
    echo(bot,update);
    user_details['daily_rate'] = update.message.text;
    # add_user details
    return JOBS;


def get_employer_contact_person(bot,update):
    echo(bot,update);
    return POSTJOBS;

def skip_employer_contact_person(bot,update):
    echo(bot,update);
    return POSTJOBS;


def show_workers_speciality(bot,update):
    echo(bot,update);
    return JOBS;

def show_available_jobs(bot,update):
    echo(bot,update);
    update.message.reply_text('.......List available jobs....\n')
    return ConversationHandler.END;

def post_jobs(bot,update):
    echo(bot,update);
    update.message.reply_text(".... Posting Jobs .....\n")
    return ConverstionHandler.END;
def show_available_employers(bot,update):
    pass;


def cancel(bot,update):
    echo(bot,update);
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END


def help(bot,update):
    echo(bot,update);
    update.message.reply_text('Help\n');

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            DECISION: [RegexHandler('^(Job_Seeker|Employer|Cancel)$', decision)],
            WORKER:[RegexHandler('^Enroll|Available Jobs|Employers$', worker)],
            EMPLOYER:[RegexHandler('^Enroll|Post Jobs|Workers$', employer_co)],
            PHONE:[MessageHandler(Filters.text, get_phone_no)],
            EMAIL:[MessageHandler(Filters.text,get_email),
                   MessageHandler('skip',skip_email)],
            SPECIALITY:[MessageHandler(Filters.text,get_worker_speciality)],
            DAILYRATE:[MessageHandler(Filters.text,get_worker_daily_rate)],
            JOBS:[MessageHandler(Filters.text,show_available_jobs)],
            POSTJOBS:[MessageHandler(Filters.text,post_jobs)],

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
