#!/usr/bin/python
"""Login and post to a Drupal CMS web site."""
import urllib
import subprocess
import os
import textwrap
import sys
from termcolor import colored
import commands
import datetime
from shutil import move
from shutil import rmtree
import gzip

# Check if root
def check_whoami():
    """Check if root"""
    if commands.getoutput( "whoami" ) != "root":
        sys.exit(colored("\tSorry, You must be root!\n", "red" ))

def uname_report():
    """Generate uname -a"""
    p = subprocess.Popen("uname -a > /tmp/uname.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def uptime_report():
    """Generate uptime"""
    p = subprocess.Popen("uptime > /tmp/uptime.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def wm_version():
    """Generate window mamnager and version"""
    path = "/etc/X11/Sessions"
    lsdir = os.listdir(path)
    for fname in lsdir:
        if fname == "Gnome":
            p = subprocess.Popen(
                    "gnome-about --version | sed 's/gnome-about//' > /tmp/window_manager.txt", 
                    shell=True, stdout=subprocess.PIPE)
            return p.stdout.readlines()
        elif fname == "kde-3.5":
            p = subprocess.Popen(
                    "kde-config --version >> /tmp/window_manager.txt", 
                    shell=True, stdout=subprocess.PIPE)
            return p.stdout.readlines()
        elif fname == "kde-4.1":
            p = subprocess.Popen(
                    "kde4-config --version >> /tmp/window_manager.txt", 
                    shell=True, stdout=subprocess.PIPE)
            return p.stdout.readlines()
        elif fname == "kde-4.2":
            p = subprocess.Popen(
                    "kde4-config --version >> /tmp/window_manager.txt", 
                    shell=True, stdout=subprocess.PIPE)
            return p.stdout.readlines()
        elif fname == "openbox":
            p = subprocess.Popen(
                    "openbox --version | sed '1!d' >> /tmp/window_manager.txt", 
                    shell=True, stdout=subprocess.PIPE)
            return p.stdout.readlines()
        elif fname == "fluxbox":
            p = subprocess.Popen(
                    "fluxbox -version >> /tmp/window_manager.txt", 
                    shell=True, stdout=subprocess.PIPE)
            return p.stdout.readlines()
        else:
            fname = '/tmp/window_manager.txt'
            fobj = open(fname, 'w')
            fobj.write('Unable to determine Window Manager.')
            fobj.close()
 
def disk_report():
    """Generate disk usage and mount points"""
    p = subprocess.Popen("df -h > /tmp/disk_report.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def rcupdate_report():
    """Generate Gentoo spacific command rc-update show"""
    p = subprocess.Popen("rc-update show > /tmp/rc_update.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()
 
def cpuinfo_report():
    """Generate cpu information"""
    p = subprocess.Popen("cat /proc/cpuinfo > /tmp/cpu_info.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def emerge_report():
    """Generate Gentoo spicific command emerge --info"""
    p = subprocess.Popen("emerge --info > /tmp/emerge_info.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def lspci_report():
    """Generate pci bus information"""
    p = subprocess.Popen("lspci > /tmp/lspci.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def lsusb_report():
    """Generate usb bus information"""
    p = subprocess.Popen("lsusb > /tmp/lsusb.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def rcconf_report():
    """OpenRC configuration file"""
    p = subprocess.Popen(
            "sed '/^[[:space:]]*\($\|#\)/d' /etc/rc.conf > /tmp/rc.conf.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def xorg_report():
    """xorg-server configuration file"""
    p = subprocess.Popen(
            "sed '/^[[:space:]]*\($\|#\)/d' /etc/X11/xorg.conf > /tmp/xorg.conf.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def net_report():
    """/etc/conf.d/net configuration file"""
    p = subprocess.Popen(
            "sed '/^[[:space:]]*\($\|#\)/d' /etc/conf.d/net > /tmp/net.txt", 
            shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def kernel_config():
    """Add kernel .config to report"""
    config_file = '/proc/config.gz'
    if os.path.exists(config_file):
        input_file = gzip.open(config_file, 'rb')
        kconfig = input_file.read()
        try:
            fname = '/tmp/kernel_config.txt'
            fobj = open(fname, 'w')
            fobj.write(kconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        input_file = '/usr/src/linux/.config'
        if os.path.exists(input_file):
            kconfig = open(input_file, 'rb')
            data = kconfig.read()
            kconfig.close()
            fname = '/tmp/kernel_config.txt'
            fobj = open(fname, 'w')
            fobj.write(data)
            fobj.close()

def alsa_config():
    """/etc/modules.d/alsa configuration file"""
    filename = '/etc/modprobe.d/alsa.conf'
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        aconfig = input_file.read()
        try:
            fname = '/tmp/alsa_conf.txt'
            fobj = open(fname, 'w')
            fobj.write(aconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        fname = '/tmp/alsa_conf.txt'
        fobj = open(fname, 'w')
        fobj.write('/etc/modprobe.d/alsa.conf not found')
        fobj.close()

def keywords():
    """/etc/portage/package.keywords"""
    filename = '/etc/portage/package.keywords'
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        aconfig = input_file.read()
        try:
            fname = '/tmp/package_keywords.txt'
            fobj = open(fname, 'w')
            fobj.write(aconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        fname = '/tmp/package_keywords.txt'
        fobj = open(fname, 'w')
        fobj.write('/etc/portage/package.keywords not found')
        fobj.close()


def use():
    """/etc/portage/package.use"""
    filename = '/etc/portage/package.use'
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        aconfig = input_file.read()
        try:
            fname = '/tmp/package_use.txt'
            fobj = open(fname, 'w')
            fobj.write(aconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        fname = '/tmp/package_use.txt'
        fobj = open(fname, 'w')
        fobj.write('/etc/portage/package.use not found')
        fobj.close()

def mask():
    """/etc/portage/package.mask"""
    filename = '/etc/portage/package.mask'
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        aconfig = input_file.read()
        try:
            fname = '/tmp/package_mask.txt'
            fobj = open(fname, 'w')
            fobj.write(aconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        fname = '/tmp/package_mask.txt'
        fobj = open(fname, 'w')
        fobj.write('/etc/portage/package.mask not found')
        fobj.close()

def unmask():
    """/etc/portage/package.unmask"""
    filename = '/etc/portage/package.unmask'
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        aconfig = input_file.read()
        try:
            fname = '/tmp/package_unmask.txt'
            fobj = open(fname, 'w')
            fobj.write(aconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        fname = '/tmp/package_unmask.txt'
        fobj = open(fname, 'w')
        fobj.write('/etc/portage/package.unmask not found')
        fobj.close()

def provided():
    """/etc/portage/package.provided"""
    filename = '/etc/portage/package.provided'
    if os.path.exists(filename):
        input_file = open(filename, 'rb')
        aconfig = input_file.read()
        try:
            fname = '/tmp/package_provided.txt'
            fobj = open(fname, 'w')
            fobj.write(aconfig)
            fobj.close()
        finally:
            input_file.close()
    else:
        fname = '/tmp/package_provided.txt'
        fobj = open(fname, 'w')
        fobj.write('/etc/portage/package.provided not found')
        fobj.close()

def create_date():
    """Add current date to bottom of report"""
    now = datetime.datetime.today()
    date = now.strftime('%h %d %Y %H:%M:%S')
    handle = open('/tmp/data.txt','a')
    logline = []
    logline.append(date)
    handle.write((' '.join(logline))+'\n')
    handle.close()        

def load_files(filename):
    """Get files and put them in username directory"""
    dir = '/tmp/' + username
    try:
        os.mkdir(dir)
        print colored('Created new directory', 'green'), dir
    except OSError, e:
        pass
    finally:
        fname = '/tmp/' + filename
        move(fname, dir)

def sendall(files):
    for name in files:
        load_files(name)

def grabfiles():
    files=['data.txt', 'uname.txt', 'window_manager.txt', 
            'disk_report.txt', 'rc_update.txt', 'cpu_info.txt', 
            'emerge_info.txt', 'lspci.txt', 'rc.conf.txt', 
            'xorg.conf.txt', 'uptime.txt', 'kernel_config.txt', 
            'net.txt', 'alsa_conf.txt', 'package_keywords.txt', 
            'package_mask.txt', 'package_unmask.txt', 'lsusb.txt',
            'package_use.txt', 'package_provided.txt']
    sendall(files)

def getdata():
    """Run all the functions from above"""
    runit = ['uname_report()', 'uptime_report()', 'disk_report()', 
            'wm_version()', 'rcupdate_report()', 'cpuinfo_report()', 
            'emerge_report()', 'lspci_report()', 'lsusb_report()', 
            'rcconf_report()', 'xorg_report()', 'kernel_config()', 
            'net_report()', 'alsa_config()', 'keywords()', 'mask()', 
            'unmask()', 'provided()', 'use()', 'create_date()']
    for i in runit:
        exec i

def show_location():
    if os.path.exists('/tmp/' + username + '/'):
        print colored('Your report has been created: %s', 'white') % '/tmp/'+ username + '/'
    else:
        print colored('\nError!, Report not found\n', 'red')

def run():    
    info = [username, '\n', make, '\n', model, '\n']
    filename = '/tmp/data.txt'
    if os.path.exists(filename):
        getdata()
        grabfiles()
        show_location()
    else:
        fobj = open(filename, "w")
        for i in info:
            fobj.write(i)
        fobj.close()
        getdata()
        grabfiles()
        show_location()

        
###########################################################################
################## Get Info and Post ######################################
###########################################################################


# get user information, check if root, load data, login and post to web site
check_whoami()

try:
    import pycurl
except ImportError:
    print 'Hi, you will need to install dev-python/pycurl.'
    print 'Goodbye'
    sys.exit()

try:
    print 'Press Control C to exit.\n'

    username = raw_input(colored('Enter your username on gentooligans.com >>> ',
        'white'))
    password = raw_input(colored('Enter your password on gentooligans.com >>> ',
        'white'))
    make = raw_input(colored('Enter the make of your computer >>> ', 'white'))
    model = raw_input(colored('Enter the model of your computer >>> ', 'white'))

    
    print colored('Now we need a hostname | unigue id name!', 'red')
    print colored('It must be all letters no punctuations!', 'green')
    get_hostname = raw_input(colored('Enter a hostname >>> ', 'white'))
    
    report_path = '/tmp/' + username + '/emerge_info.txt'
    cpu_report_path = '/tmp/' + username + '/cpu_info.txt'
    disk_report_path = '/tmp/' + username + '/disk_report.txt'
    net_report_path = '/tmp/' + username + '/net.txt'
    rc_report_path = '/tmp/' + username + '/rc.conf.txt'
    rc_update_report_path = '/tmp/' + username + '/rc_update.txt'
    xorg_report_path = '/tmp/' + username + '/xorg.conf.txt'
    keyword_report_path = '/tmp/' + username + '/package_keywords.txt'
    use_report_path = '/tmp/' + username + '/package_use.txt'
    mask_report_path = '/tmp/' + username + '/package_mask.txt'
    unmask_report_path = '/tmp/' + username + '/package_unmask.txt'
    provided_report_path = '/tmp/' + username + '/package_provided.txt'

except KeyboardInterrupt:
    print '\nGoodbye\n'
    sys.exit()

dir = '/tmp/' + username
if os.path.exists(dir):
    rmtree(dir)

if username:
    pass
else:
    print 'You must enter a username!'
    print 'Try Again!'
    sys.exit()

if password:
    pass
else:
    print 'You must enter a password!'
    print 'Try Again!'
    sys.exit()

run()
if os.path.exists(report_path):
    pass
else:
    print 'Report Not Found!'
    print 'Goodbye!'
    sys.exit()

if get_hostname == '':
    pass
else:
    HOSTNAME = get_hostname

print colored('OK Looks Good, continuing ...', 'yellow')

token_file = open('/tmp/token_file', 'w')
hosts_token_file = open('/tmp/hosts_token_file', 'w')
cpu_token_file = open('/tmp/cpu_token_file', 'w')
fstab_token_file = open('/tmp/fstab_token_file', 'w')
net_token_file = open('/tmp/net_token_file', 'w')
rc_token_file = open('/tmp/rc_token_file', 'w')
rc_update_token_file = open('/tmp/rc_update_token_file', 'w')
xorg_token_file = open('/tmp/xorg_token_file', 'w')
alsa_token_file = open('/tmp/alsa_token_file', 'w')
package_token_file = open('/tmp/package_token_file', 'w')
user_agent = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.5) \
Gecko/2008121718 Gentoo Firefox/3.0.5'
login = [('name', username), ('pass', password), ('form_id', 'user_login'), ('op', 'Log in')]
login_data = urllib.urlencode(login)

# Login  
crl = pycurl.Curl()
crl.setopt(pycurl.POSTFIELDS, login_data)
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/?q=user')
crl.setopt(pycurl.USERAGENT, user_agent)
crl.setopt(pycurl.COOKIEFILE, '/tmp/cookie.txt')
crl.setopt(pycurl.COOKIEJAR, '/tmp/cookie.txt')
crl.perform()

# Retrieve and store token, should return 200  
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/node/add/gentoo-hosts')
crl.setopt(pycurl.FILE, hosts_token_file)
crl.perform()

proc = subprocess.Popen(
        'grep edit-gentoo-hosts-node-form-form-token /tmp/hosts_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
hosts_token = proc.stdout.read().strip()

hostname_node = [('title', HOSTNAME), ('changed', ''), ('form_build_id', ''), 
        ('form_token', hosts_token), ('form_id', 'gentoo_hosts_node_form'), ('op', 'Save')]

# Post Hostname, need to post hostname as final report post used HOSTNAME as Title
# Should return 302
hostname_data = urllib.urlencode(hostname_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, hostname_data)
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/node/add/gentoo-hosts')
crl.setopt(pycurl.FILE, hosts_token_file)
crl.perform()

# The hostname value is a number, grap and store that page, should return 200
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/' + username + '/host/' + HOSTNAME)
crl.setopt(pycurl.FILE, hosts_token_file)
crl.perform()

#  Get Hostname number from stored page
proc = subprocess.Popen(
        'grep "#node-" /tmp/hosts_token_file |head -n1|cut -d\- -f4', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
hosts_number = proc.stdout.read().strip()

print colored('Sorry for all the noise.', 'cyan')
print
print colored('Getting required tokens.', 'white')
print
print colored('OK posting to gentooligans, please wait!', 'green')

# Retrieve and store token for make_conf post form
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/node/add/gentoo-report-makeconf')
crl.setopt(pycurl.FILE, token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-makeconf-node-form-form-token /tmp/token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
token = proc.stdout.read().strip()

# Did LINGUAS alone because it was pulling in USE values
fname = open(report_path)
for line in fname:
    if 'LINGUAS' in line:
        output = line.split('"')[1]
        LINGUAS = textwrap.fill(output, 80)
        break
    else:
        LINGUAS = ''
fname.close()

# Get USE
fname = open(report_path)
for line in fname:
    if 'USE=' in line:
        output = line.split('"')[1]
        USE = textwrap.fill(output, 80)
        break
    else:
        USE = ''
fname.close()

# Get Portage
fname = open(report_path)
for line in fname:
    if 'Portage' in line:
        PORTAGE = line
        break
    else:
        PORTAGE = ''
fname.close()

# Get System Name
fname = open(report_path)
for line in fname:
    if 'System' in line:
        SYSTEM_NAME = line
        break
    else:
        SYSTEM_NAME = ''
fname.close()

# Get Timestamp
fname = open(report_path)
for line in fname:
    if 'Timestamp' in line:
        TIMESTAMP = line
        break
    else:
        TIMESTAMP = ''
fname.close()

# Get data for packages fields

search_terms = ['app-shells/bash:', 'dev-java/java-config:', 'dev-lang/python:', 
        'dev-python/pycrypto:', 'dev-util/ccache:', 'dev-util/cmake:', 'sys-apps/baselayout:', 
        'sys-apps/openrc:', 'sys-apps/sandbox:', 'sys-devel/autoconf:', 'sys-devel/automake:', 
        'sys-devel/binutils:', 'sys-devel/gcc-config:', 'sys-devel/libtool:', 'virtual/os-headers:']

fname = open(report_path)
tmp_file = '/tmp/package_list.txt'
for line in fname:
    if search_terms[0] in line:
        bash = line.strip()
    else:
        bash = ''
    if search_terms[1] in line:
        java = line.strip()
    else:
        java = ''
    if search_terms[2] in line:
        python = line.strip()
    else:
        python = ''
    if search_terms[3] in line:
        pycrypto = line.strip()
    else:
        pycrypto = ''
    if search_terms[4] in line:
        ccache = line.strip()
    else:
        ccache = ''
    if search_terms[5] in line:
        cmake = line.strip()
    else:
        cmake = ''
    if search_terms[6] in line:
        baselayout = line.strip()
    else:
        baselayout = ''
    if search_terms[7] in line:
        openrc = line.strip()
    else:
        openrc = ''
    if search_terms[8] in line:
        sandbox = line.strip()
    else:
        sandbox = ''
    if search_terms[9] in line:
        autoconf = line.strip()
    else:
        autoconf = ''
    if search_terms[10] in line:
        automake = line.strip()
    else:
        automake = ''
    if search_terms[11] in line:
                binutils = line.strip()
    else:
        binutils = ''
    if search_terms[12] in line:
            gcc_config = line.strip()
    else:
        gcc_config = ''
    if search_terms[13] in line:
        libtool = line.strip()
    else:
        libtool = ''
    if search_terms[14] in line:
        os_headers = line.strip()
    else:
        os_headers = ''

info = [bash, '\n', java, '\n', python, '\n', pycrypto, '\n', ccache, '\n', 
        cmake, '\n', baselayout, '\n', openrc, '\n', sandbox, '\n', autoconf, '\n', 
        automake, '\n', binutils, '\n', gcc_config, '\n', libtool, '\n', os_headers, '\n']


# Write data to tmp file
tmp_obj = open(tmp_file, 'w')
for i in info:
    tmp_obj.write(i)
fname.close
tmp_obj.close()

# Open tmp file for reading
fname = open(tmp_file, 'rb')
PACKAGES = fname.read()
fname.close()

# Loop over dict keys
data = {'ACCEPT_KEYWORDS':None, 'CBUILD':None, 'CFLAGS':None, 
        'CHOST':None, 'CXXFLAGS':None, 'FEATURES':None, 
        'LDFLAGS':None, 'MAKEOPTS':None}

def get_values():
    fname = open(report_path)
    for line in fname:
        for keyphrase in data:
            if keyphrase in line:
                output = line.split('"')[1]
                data[keyphrase] = textwrap.fill(output, 80)
    fname.close()
get_values()

# make_conf post should return 302
node = [('field_hostname[nid][nid]', hosts_number), ('field_portage[0][value]', PORTAGE), 
        ('field_timestamp_of_tree[0][value]', TIMESTAMP), ('field_system_uname[0][value]', SYSTEM_NAME), 
        ('changed', ''), ('form_build_id', ''), ('form_token', token), ('form_id', 'gentoo_report_makeconf_node_form'), 
        ('field_packages[0][value]', PACKAGES), ('field_accepted_keywords[0][value]', data['ACCEPT_KEYWORDS']), 
        ('field_cbuild[0][value]', data['CBUILD']), ('field_cflags[0][value]', data['CFLAGS']), 
        ('field_chost[0][value]', data['CHOST']), ('field_cxxflags[0][value]', data['CXXFLAGS']), 
        ('field_make_features[0][value]', data['FEATURES']), ('field_ldflags[0][value]', data['LDFLAGS']), 
        ('field_linguas[0][value]', LINGUAS), ('field_makeopts[0][value]', data['MAKEOPTS']), 
        ('field_use[0][value]', USE), ('field_alsa_cards[0][value]', ''), ('field_alsa_pcm_plugins[0][value]', ''), 
        ('form_id', 'gentoo_report_makeconf_node_form'), ('op', 'Save')]
node_data = urllib.urlencode(node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, node_data)
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/node/add/gentoo-report-makeconf')
crl.perform()

# Retrieve and store token for cpuinfo post form
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/node/add/gentoo-report-cpuinfo')
crl.setopt(pycurl.FILE, cpu_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-cpuinfo-node-form-form-token /tmp/cpu_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
cpu_token = proc.stdout.read().strip()

# Create title
proc = subprocess.Popen(
        "sed -n 5p /proc/cpuinfo | awk '{print$4, $5, $6, $7, $8, $9}'", 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
cpu = proc.stdout.read().strip()
Title = HOSTNAME + ' : ' + cpu

# Create body
cpufile = open(cpu_report_path, 'rb')
body = cpufile.read()

# cpu_info should return 302
cpu_node = [('field_hostname[nid][nid]', hosts_number), ('title', Title), ('body', body), ('form_build_id', ''),
        ('form_token', cpu_token), ('form_id', 'gentoo_report_cpuinfo_node_form'), ('op', 'save')]
cpu_node_data = urllib.urlencode(cpu_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, cpu_node_data)
crl.setopt(pycurl.URL, 'http://beta.gentooligans.com/node/add/gentoo-report-cpuinfo')
crl.perform()

# Retrieve and store token for fstab post form
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-fstab')
crl.setopt(pycurl.FILE, fstab_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-fstab-node-form-form-token /tmp/fstab_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
fstab_token = proc.stdout.read().strip()

# Create Body
proc = subprocess.Popen('cat /etc/fstab | grep /dev', shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
fstab = proc.stdout.read().strip()

# Create body
fstabfile = open(disk_report_path, 'rb')
fbody = fstabfile.read()
disk_body = fstab + '\n\n' + fbody
fstab_title = HOSTNAME + ' : ' + 'Disk Report'

# fstab should return 302
fstab_node = [('field_hostname[nid][nid]', hosts_number),('title', fstab_title), 
        ('body', disk_body), ('form_build_id', ''), ('form_token', fstab_token), 
        ('form_id', 'gentoo_report_fstab_node_form'), ('op', 'Save')]
fstab_node_data = urllib.urlencode(fstab_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, fstab_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-fstab')
crl.perform()

# Retrieve and store token for net post form
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-net')
crl.setopt(pycurl.FILE, net_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-net-node-form-form-token /tmp/net_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
net_token = proc.stdout.read().strip()

# Create body
netfile = open(net_report_path, 'rb')
net_body = netfile.read()
net_title = HOSTNAME + ' : ' + 'Network Report'

# net should return 302
net_node = [('field_hostname[nid][nid]', hosts_number),('title', net_title), 
        ('body', net_body), ('form_build_id', ''), ('form_token', net_token), 
        ('form_id', 'gentoo_report_net_node_form'), ('op', 'Save')]
net_node_data = urllib.urlencode(net_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, net_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-net')
crl.perform()

# Retrieve and store token for rc.conf post form
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-rc')
crl.setopt(pycurl.FILE, rc_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-rc-node-form-form-token /tmp/rc_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
rc_token = proc.stdout.read().strip()

# Create body
rcfile = open(rc_report_path, 'rb')
rc_body = rcfile.read()
rc_title = HOSTNAME + ' : ' + 'rc.conf Report'

# net should return 302
rc_node = [('field_hostname[nid][nid]', hosts_number),('title', rc_title), 
        ('body', rc_body), ('form_build_id', ''), ('form_token', rc_token), 
        ('form_id', 'gentoo_report_rc_node_form'), ('op', 'Save')]
rc_node_data = urllib.urlencode(rc_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, rc_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-rc')
crl.perform()

# Retrieve and store token for rc_update post form
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-rcupdate')
crl.setopt(pycurl.FILE, rc_update_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-rcupdate-node-form-form-token /tmp/rc_update_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
rc_update_token = proc.stdout.read().strip()

# Create body
rc_updatefile = open(rc_update_report_path, 'rb')
rc_update_body = rc_updatefile.read()
rc_update_title = HOSTNAME + ' : ' + 'rc-update Report'

# rc_update should return 302
rc_update_node = [('field_hostname[nid][nid]', hosts_number),('title', rc_update_title), 
        ('body', rc_update_body), ('form_build_id', ''), ('form_token', rc_update_token), 
        ('form_id', 'gentoo_report_rcupdate_node_form'), ('op', 'Save')]
rc_update_node_data = urllib.urlencode(rc_update_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, rc_update_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-rcupdate')
crl.perform()

# Retrieve and store token for xorg.conf post form
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-xorgconf')
crl.setopt(pycurl.FILE, xorg_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-xorgconf-node-form-form-token /tmp/xorg_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
xorg_token = proc.stdout.read().strip()

# Create body
xorgfile = open(xorg_report_path, 'rb')
xorg_body = xorgfile.read()
xorg_title = HOSTNAME + ' : ' + 'xorg.conf Report'

# xorg should return 302
xorg_node = [('field_hostname[nid][nid]', hosts_number),('title', xorg_title), 
        ('body', xorg_body), ('form_build_id', ''), ('form_token', xorg_token), 
        ('form_id', 'gentoo_report_xorgconf_node_form'), ('op', 'Save')]
xorg_node_data = urllib.urlencode(xorg_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, xorg_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-xorgconf')
crl.perform()

# Retrieve and store token for pkg-info post form
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-pkg-info')
crl.setopt(pycurl.FILE, package_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-pkg-info-node-form-form-token /tmp/package_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
pkg_token = proc.stdout.read().strip()

# Create body
keywordfile = open(keyword_report_path, 'rb')
usefile = open(use_report_path, 'rb')
maskfile = open(mask_report_path, 'rb')
unmaskfile = open(unmask_report_path, 'rb')
providedfile = open(provided_report_path, 'rb')

keyword_body = keywordfile.read()
use_body = usefile.read()
mask_body = maskfile.read()
unmask_body = unmaskfile.read()
provided_body = providedfile.read()

pkg_title = HOSTNAME + ' : ' + 'pkg-info Report'

# xorg should return 302
pkg_node = [('field_hostname[nid][nid]', hosts_number), 
        ('field_p_keywords[0][value]', keyword_body), 
        ('field_p_use[0][value]', use_body), 
        ('field_p_mask[0][value]', mask_body), 
        ('field_p_unmask[0][value]', unmask_body), 
        ('field_p_provided[0][value]', provided_body), 
        ('form_build_id', ''), 
        ('form_token', pkg_token), 
        ('form_id', 'gentoo_report_pkg_info_node_form'), 
        ('op', 'Save')]
pkg_node_data = urllib.urlencode(pkg_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, pkg_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-pkg-info')
crl.perform()

def alsa():
    alsa_report_path = '/tmp/' + username + '/alsa_conf.txt'
    alsa_tmp_file = '/tmp/alsa_list.txt'
    
    #  Get ALSA_CARDS from emerge --info
    proc = subprocess.Popen(
            'cat /tmp/comprookie2000/emerge_info.txt | grep ALSA_CARDS= |cut -d \\" -f4', 
            shell=True, stdout=subprocess.PIPE,)
    os.waitpid(proc.pid, 0)
    ALSA_CARDS = proc.stdout.read().strip()

    # Get ALSA_PCM_PLUGINS from emerge --info
    proc = subprocess.Popen(
            'cat /tmp/comprookie2000/emerge_info.txt | grep ALSA_PCM_PLUGINS= |cut -d\\" -f6', 
            shell=True, stdout=subprocess.PIPE,)
    os.waitpid(proc.pid, 0)
    ALSA_PCM_PLUGINS = proc.stdout.read().strip()

    # Create body for post
    alsafile = open(alsa_report_path, 'rb')
    alsa_body = alsafile.read()
    
    # Completed body
    alsa_info = ['ALSA_CARDS=', 
            ALSA_CARDS, '\n', 
            'ALSA_PCM_PLUGINS=', 
            ALSA_PCM_PLUGINS, '\n', 
            alsa_body]

    # Write data to tmp file
    tmp_obj = open(alsa_tmp_file, 'w')
    for i in alsa_info:
        tmp_obj.write(i)
    tmp_obj.close()

    # Clean up comments and blank spaces
    proc = subprocess.Popen(
            "sed -e '/^\##/d' -e '/^ *$/d' /tmp/alsa_list.txt", 
            shell=True, stdout=subprocess.PIPE,)
    os.waitpid(proc.pid, 0)
    alsa_body = proc.stdout.read().strip()
    return alsa_body

alsa_title = HOSTNAME + ' : ' + 'Alsa Report'
alsa_body = alsa()

# Retrieve and store token for alsa post form

crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-alsa')
crl.setopt(pycurl.FILE, alsa_token_file)
crl.perform()

# Get token from stored page
proc = subprocess.Popen(
        'grep edit-gentoo-report-alsa-node-form-form-token /tmp/alsa_token_file |cut -d\\" -f8', 
        shell=True, stdout=subprocess.PIPE,)
os.waitpid(proc.pid, 0)
alsa_token = proc.stdout.read().strip()

# xorg should return 302
alsa_node = [('field_hostname[nid][nid]', hosts_number),('title', alsa_title), 
        ('body', alsa_body), ('form_build_id', ''), ('form_token', alsa_token), 
        ('form_id', 'gentoo_report_alsa_node_form'), ('op', 'save')]
alsa_node_data = urllib.urlencode(alsa_node)
crl.setopt(pycurl.HTTPHEADER, ["Expect:"])
crl.setopt(pycurl.POSTFIELDS, alsa_node_data)
crl.setopt(pycurl.URL,
        'http://beta.gentooligans.com/node/add/gentoo-report-alsa')
crl.perform()


# close pycurl connection
crl.close()

# close all files
token_file.close()
hosts_token_file.close()
cpu_token_file.close()
cpufile.close()
fstab_token_file.close()
fstabfile.close()
net_token_file.close()
netfile.close
rc_token_file.close()
rcfile.close()
rc_update_token_file.close()
rc_updatefile.close()
xorg_token_file.close()
xorgfile.close()
alsa_token_file.close()
package_token_file.close()


