

  * Public/Stable/Replaceable 
    * hadoop_add_array_param
    * hadoop_add_classpath
    * hadoop_add_client_opts
    * hadoop_add_colonpath
    * hadoop_add_javalibpath
    * hadoop_add_ldlibpath
    * hadoop_add_param
    * hadoop_add_profile
    * hadoop_array_contains
    * hadoop_build_custom_subcmd_var
    * hadoop_deprecate_envvar
    * hadoop_detect_priv_subcmd
    * hadoop_java_exec
    * hadoop_java_setup
    * hadoop_mkdir
    * hadoop_need_reexec
    * hadoop_os_tricks
    * hadoop_sort_array
    * hadoop_status_daemon
    * hadoop_stop_daemon
    * hadoop_stop_secure_daemon
    * hadoop_subcommand_secure_opts
    * hadoop_translate_cygwin_path
    * hadoop_using_envvar
    * hadoop_validate_classname
    * hadoop_verify_confdir
    * hadoop_verify_user_perm
    * hadoop_verify_user_resolves
  * Public/Stable/Not Replaceable 
    * hadoop_abs
    * hadoop_add_entry
    * hadoop_debug
    * hadoop_delete_entry
    * hadoop_error
    * hadoop_exit_with_usage
    * hadoop_populate_workers_file
    * hadoop_rotate_log
    * hadoop_verify_entry
  * Public/Evolving/Replaceable 
    * hadoop_subcommand_opts
  * Private/Evolving/Replaceable 
    * hadoop_actual_ssh
    * hadoop_add_common_to_classpath
    * hadoop_add_to_classpath_tools
    * hadoop_add_to_classpath_userpath
    * hadoop_common_worker_mode_execute
    * hadoop_connect_to_hosts
    * hadoop_connect_to_hosts_without_pdsh
    * hadoop_daemon_handler
    * hadoop_do_classpath_subcommand
    * hadoop_exec_hadooprc
    * hadoop_exec_user_hadoopenv
    * hadoop_finalize
    * hadoop_finalize_classpath
    * hadoop_finalize_hadoop_heap
    * hadoop_finalize_hadoop_opts
    * hadoop_finalize_libpaths
    * hadoop_generic_java_subcmd_handler
    * hadoop_import_shellprofiles
    * hadoop_parse_args
    * hadoop_privilege_check
    * hadoop_secure_daemon_handler
    * hadoop_setup_secure_service
    * hadoop_shellprofiles_classpath
    * hadoop_shellprofiles_finalize
    * hadoop_shellprofiles_init
    * hadoop_shellprofiles_nativelib
    * hadoop_start_daemon
    * hadoop_start_daemon_wrapper
    * hadoop_start_secure_daemon
    * hadoop_start_secure_daemon_wrapper
    * hadoop_su
    * hadoop_verify_logdir
    * hadoop_verify_piddir
    * hadoop_verify_secure_prereq



* * *

## Public/Stable/Replaceable

### hadoop_add_array_param

  * Synopsis


    
    
    hadoop_add_array_param envvar appendstring
    

  * Description



Add the appendstring if checkstring is not present in the given array

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_classpath

  * Synopsis


    
    
    hadoop_add_classpath object [before|after]
    

  * Description



Add a file system object (directory, file, wildcard, …) to the classpath. Optionally provide a hint as to where in the classpath it should go.

  * Returns



0 = success (added or duplicate)

1 = failure (doesn’t exist or some other reason)

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_client_opts

  * Synopsis


    
    
    hadoop_add_client_opts
    

  * Description



Adds the HADOOP_CLIENT_OPTS variable to HADOOP_OPTS if HADOOP_SUBCMD_SUPPORTDAEMONIZATION is false

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_colonpath

  * Synopsis


    
    
    hadoop_add_colonpath envvar object [before|after]
    

  * Description



Add a file system object (directory, file, wildcard, …) to the colonpath. Optionally provide a hint as to where in the colonpath it should go. Prior to adding, objects are checked for duplication and check for existence. Many other functions use this function as their base implementation including hadoop_add_javalibpath and hadoop_add_ldlibpath.

  * Returns



0 = success (added or duplicate)

1 = failure (doesn’t exist or some other reason)

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_javalibpath

  * Synopsis


    
    
    hadoop_add_javalibpath object [before|after]
    

  * Description



Add a file system object (directory, file, wildcard, …) to the Java JNI path. Optionally provide a hint as to where in the Java JNI path it should go.

  * Returns



0 = success (added or duplicate)

1 = failure (doesn’t exist or some other reason)

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_ldlibpath

  * Synopsis


    
    
    hadoop_add_ldlibpath object [before|after]
    

  * Description



Add a file system object (directory, file, wildcard, …) to the LD_LIBRARY_PATH. Optionally provide a hint as to where in the LD_LIBRARY_PATH it should go.

  * Returns



0 = success (added or duplicate)

1 = failure (doesn’t exist or some other reason)

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_param

  * Synopsis


    
    
    hadoop_add_param envvar checkstring appendstring
    

  * Description



Append the appendstring if checkstring is not present in the given envvar

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_add_profile

  * Synopsis


    
    
    hadoop_add_profile shellprofile
    

  * Description



Register the given shellprofile to the Hadoop shell subsystem

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_array_contains

  * Synopsis


    
    
    hadoop_array_contains element array
    

  * Description



Check if an array has a given value

  * Returns



## @returns 0 = yes

## @returns 1 = no

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_build_custom_subcmd_var

  * Synopsis


    
    
    hadoop_build_custom_subcmd_var command subcommand customid
    

  * Description



Build custom subcommand var

  * Returns



string

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_deprecate_envvar

  * Synopsis


    
    
    hadoop_deprecate_envvar oldvar newvar
    

  * Description



Replace oldvar with newvar if oldvar exists.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_detect_priv_subcmd

  * Synopsis


    
    
    hadoop_detect_priv_subcmd command subcommand
    

  * Description



autodetect whether this is a priv subcmd by whether or not a priv user var exists and if HADOOP_SECURE_CLASSNAME is defined

  * Returns



1 = not priv

0 = priv

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_java_exec

  * Synopsis


    
    
    hadoop_java_exec command class [options]
    

  * Description



Execute the Java class, passing along any options. Additionally, set the Java property -Dproc_command.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_java_setup

  * Synopsis


    
    
    hadoop_java_setup
    

  * Description



Configure/verify ${JAVA_HOME}

  * Returns



may exit on failure conditions

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_mkdir

  * Synopsis


    
    
    hadoop_mkdir dir
    

  * Description



Create the directory ‘dir’.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_need_reexec

  * Synopsis


    
    
    hadoop_need_reexec subcommand
    

  * Description



Verify that ${USER} is allowed to execute the given subcommand.

  * Returns



1 on no re-exec needed

0 on need to re-exec

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_os_tricks

  * Synopsis


    
    
    hadoop_os_tricks
    

  * Description



Routine to configure any OS-specific settings.

  * Returns



may exit on failure conditions

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_sort_array

  * Synopsis


    
    
    hadoop_sort_array arrayvar
    

  * Description



Sort an array (must not contain regexps) present in the given array

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_status_daemon

  * Synopsis


    
    
    hadoop_status_daemon pidfile
    

  * Description



Determine the status of the daemon referenced by pidfile

  * Returns



(mostly) LSB 4.1.0 compatible status

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_stop_daemon

  * Synopsis


    
    
    hadoop_stop_daemon command pidfile
    

  * Description



Stop the non-privileged command daemon with that that is running at pidfile.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_stop_secure_daemon

  * Synopsis


    
    
    hadoop_stop_secure_daemon command daemonpidfile wrapperpidfile
    

  * Description



Stop the privileged command daemon with that that is running at daemonpidfile and launched with the wrapper at wrapperpidfile.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_subcommand_secure_opts

  * Synopsis


    
    
    hadoop_subcommand_secure_opts program subcommand
    

  * Description



Add custom (program)_(command)_SECURE_EXTRA_OPTS to HADOOP_OPTS. This does not handle the pre-3.x deprecated cases

  * Returns



will exit on failure conditions

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_translate_cygwin_path

  * Synopsis


    
    
    hadoop_translate_cygwin_path varnameref [true]
    

  * Description



Converts the contents of the variable name varnameref into the equivalent Windows path. If the second parameter is true, then varnameref is treated as though it was a path list.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_using_envvar

  * Synopsis


    
    
    hadoop_using_envvar var
    

  * Description



Declare var being used and print its value.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_validate_classname

  * Synopsis


    
    
    hadoop_validate_classname classname
    

  * Description



Verify that a shell command was passed a valid class name

  * Returns



0 = success

1 = failure w/user message

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_verify_confdir

  * Synopsis


    
    
    hadoop_verify_confdir
    

  * Description



Validate ${HADOOP_CONF_DIR}

  * Returns



will exit on failure conditions

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_verify_user_perm

  * Synopsis


    
    
    hadoop_verify_user_perm command subcommand
    

  * Description



Verify that ${USER} is allowed to execute the given subcommand.

  * Returns



return 0 on success

exit 1 on failure

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
### hadoop_verify_user_resolves

  * Synopsis


    
    
    hadoop_verify_user_resolves userstring
    

  * Description



Verify that username in a var converts to user id

  * Returns



0 for success

1 for failure

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  Yes   
  
## Public/Stable/Not Replaceable

### hadoop_abs

  * Synopsis


    
    
    hadoop_abs fsobj
    

  * Description



Given a filename or dir, return the absolute version of it This works as an alternative to readlink, which isn’t portable.

  * Returns



0 success

1 failure

stdout abspath

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_add_entry

  * Synopsis


    
    
    hadoop_add_entry
    

  * Description



Given variable $1 add $2 to it

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_debug

  * Synopsis


    
    
    hadoop_debug string
    

  * Description



Print a message to stderr if –debug is turned on

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_delete_entry

  * Synopsis


    
    
    hadoop_delete_entry
    

  * Description



Given variable $1 delete $2 from it

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_error

  * Synopsis


    
    
    hadoop_error string
    

  * Description



Print a message to stderr

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_exit_with_usage

  * Synopsis


    
    
    hadoop_exit_with_usage exitcode
    

  * Description



Print usage information and exit with the passed exitcode

  * Returns



This function will always exit.

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_populate_workers_file

  * Synopsis


    
    
    hadoop_populate_workers_file filename
    

  * Description



Set the worker support information to the contents of filename

  * Returns



will exit if file does not exist

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_rotate_log

  * Synopsis


    
    
    hadoop_rotate_log filename [number]
    

  * Description



Rotates the given file until number of files exist.

  * Returns



$? will contain last mv’s return value

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
### hadoop_verify_entry

  * Synopsis


    
    
    hadoop_verify_entry
    

  * Description



Given variable $1 determine if $2 is in it

  * Returns



0 = yes, 1 = no

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Stable   
Replaceable  |  No   
  
## Public/Evolving/Replaceable

### hadoop_subcommand_opts

  * Synopsis


    
    
    hadoop_subcommand_opts program subcommand
    

  * Description



Add custom (program)_(command)_OPTS to HADOOP_OPTS. Also handles the deprecated cases from pre-3.x.

  * Returns



will exit on failure conditions

Classification  |  Level   
---|---  
Audience  |  Public   
Stability  |  Evolving   
Replaceable  |  Yes   
  
## Private/Evolving/Replaceable

### hadoop_actual_ssh

  * Synopsis


    
    
    hadoop_actual_ssh hostname command [...]
    

  * Description



Via ssh, log into hostname and run command

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_add_common_to_classpath

  * Synopsis


    
    
    hadoop_add_common_to_classpath
    

  * Description



Add the common/core Hadoop components to the environment

  * Returns



## @returns 1 on failure, may exit

## @returns 0 on success

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_add_to_classpath_tools

  * Synopsis


    
    
    hadoop_add_to_classpath_tools module
    

  * Description



Run libexec/tools/module.sh to add to the classpath environment

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_add_to_classpath_userpath

  * Synopsis


    
    
    hadoop_add_to_classpath_userpath
    

  * Description



Add the user’s custom classpath settings to the environment

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_common_worker_mode_execute

  * Synopsis


    
    
    hadoop_common_worker_mode_execute commandarray
    

  * Description



Utility routine to handle –workers mode

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_connect_to_hosts

  * Synopsis


    
    
    hadoop_connect_to_hosts command [...]
    

  * Description



Connect to ${HADOOP_WORKERS} or ${HADOOP_WORKER_NAMES} and execute command.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_connect_to_hosts_without_pdsh

  * Synopsis


    
    
    hadoop_connect_to_hosts_without_pdsh command [...]
    

  * Description



Connect to ${HADOOP_WORKER_NAMES} and execute command under the environment which does not support pdsh.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_daemon_handler

  * Synopsis


    
    
    hadoop_daemon_handler [start|stop|status|default] command class daemonpidfile daemonoutfile [options]
    

  * Description



Manage a non-privileged daemon.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_do_classpath_subcommand

  * Synopsis


    
    
    hadoop_do_classpath_subcommand [parameters]
    

  * Description



Perform the ‘hadoop classpath’, etc subcommand with the given parameters

  * Returns



will print & exit with no params

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_exec_hadooprc

  * Synopsis


    
    
    hadoop_exec_hadooprc
    

  * Description



Read the user’s settings. This provides for users to run Hadoop Shell API after system bootstrap

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_exec_user_hadoopenv

  * Synopsis


    
    
    hadoop_exec_user_hadoopenv
    

  * Description



Read the user’s settings. This provides for users to override and/or append hadoop-env.sh. It is not meant as a complete system override.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_finalize

  * Synopsis


    
    
    hadoop_finalize
    

  * Description



Finish all the remaining environment settings prior to executing Java. This is a wrapper that calls the other finalize routines.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_finalize_classpath

  * Synopsis


    
    
    hadoop_finalize_classpath
    

  * Description



Finish Java classpath prior to execution

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_finalize_hadoop_heap

  * Synopsis


    
    
    hadoop_finalize_hadoop_heap
    

  * Description



Finish Java heap parameters prior to execution

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_finalize_hadoop_opts

  * Synopsis


    
    
    hadoop_finalize_hadoop_opts
    

  * Description



Finish configuring Hadoop specific system properties prior to executing Java

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_finalize_libpaths

  * Synopsis


    
    
    hadoop_finalize_libpaths
    

  * Description



Finish Java JNI paths prior to execution

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_generic_java_subcmd_handler

  * Synopsis


    
    
    hadoop_generic_java_subcmd_handler
    

  * Description



Handle subcommands from main program entries

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_import_shellprofiles

  * Synopsis


    
    
    hadoop_import_shellprofiles
    

  * Description



Import shellprofile.d content

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_parse_args

  * Synopsis


    
    
    hadoop_parse_args [parameters, typically "$@"]
    

  * Description



generic shell script opton parser. sets HADOOP_PARSE_COUNTER to set number the caller should shift

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_privilege_check

  * Synopsis


    
    
    hadoop_privilege_check
    

  * Description



Check if we are running with priv by default, this implementation looks for EUID=0. For OSes that have true priv separation, this should be something more complex

  * Returns



1 = no priv

0 = priv

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_secure_daemon_handler

  * Synopsis


    
    
    hadoop_secure_daemon_handler [start|stop|status|default] command class daemonpidfile daemonoutfile wrapperpidfile wrapperoutfile wrappererrfile [options]
    

  * Description



Manage a privileged daemon.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_setup_secure_service

  * Synopsis


    
    
    hadoop_setup_secure_service
    

  * Description



None

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_shellprofiles_classpath

  * Synopsis


    
    
    hadoop_shellprofiles_classpath
    

  * Description



Apply the shell profile classpath additions

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_shellprofiles_finalize

  * Synopsis


    
    
    hadoop_shellprofiles_finalize
    

  * Description



Apply the shell profile final configuration

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_shellprofiles_init

  * Synopsis


    
    
    hadoop_shellprofiles_init
    

  * Description



Initialize the registered shell profiles

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_shellprofiles_nativelib

  * Synopsis


    
    
    hadoop_shellprofiles_nativelib
    

  * Description



Apply the shell profile native library additions

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_start_daemon

  * Synopsis


    
    
    hadoop_start_daemon command class pidfile [options]
    

  * Description



Start a non-privileged daemon in the foreground.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_start_daemon_wrapper

  * Synopsis


    
    
    hadoop_start_daemon_wrapper command class pidfile outfile [options]
    

  * Description



Start a non-privileged daemon in the background.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_start_secure_daemon

  * Synopsis


    
    
    hadoop_start_secure_daemon command class daemonpidfile daemonoutfile daemonerrfile wrapperpidfile [options]
    

  * Description



Start a privileged daemon in the foreground.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_start_secure_daemon_wrapper

  * Synopsis


    
    
    hadoop_start_secure_daemon_wrapper command class daemonpidfile daemonoutfile wrapperpidfile warpperoutfile daemonerrfile [options]
    

  * Description



Start a privileged daemon in the background.

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_su

  * Synopsis


    
    
    hadoop_su user commandstring
    

  * Description



Execute a command via su when running as root if the given user is found or exit with failure if not. otherwise just run it. (This is intended to be used by the start-/stop- scripts.)

  * Returns



exitstatus

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_verify_logdir

  * Synopsis


    
    
    hadoop_verify_logdir
    

  * Description



None

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_verify_piddir

  * Synopsis


    
    
    hadoop_verify_piddir
    

  * Description



None

  * Returns



Nothing

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes   
  
### hadoop_verify_secure_prereq

  * Synopsis


    
    
    hadoop_verify_secure_prereq
    

  * Description



Verify that prerequisites have been met prior to excuting a privileged program.

  * Returns



This routine may exit.

Classification  |  Level   
---|---  
Audience  |  Private   
Stability  |  Evolving   
Replaceable  |  Yes 
