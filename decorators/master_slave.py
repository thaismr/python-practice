print()


def master():
    def slave():
        print('Slave function.')
    # We have to call slave function if we want it executed:
    slave()


master()  # Master calls slave from inside, so slave's msg is printed in the screen

print()


# If we don't call our slave function from inside our master function,
# and since we are RETURNING THE SLAVE as result of calling our master,
# we can assign (EITHER MASTER OR SLAVE) function to a variable without executing it
def f_master():
    def f_slave():
        print('Slave function f_slave.')

    return f_slave


f_master()  # prints nothing, only returns f_slave


master_copy = f_master  # master_copy == f_master!

master_copy()  # prints nothing, does the same as f_master (RETURNS f_slave)


slave_copy = f_master()  # prints nothing, but gets F_SLAVE back from calling f_master(). Now slave_copy == F_SLAVE

slave_copy()  # now equals f_slave, calling slave_copy() == calling f_slave()
