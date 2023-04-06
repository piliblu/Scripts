function leakcap(){
    dc=$(cat /usr/local/akamai/etc/.location)
    tcpdump -nni bond1 host $1 -c 300 -w $dc-bond1-$1-$(date +"%s").pcap ; tcpdump -nni bond0 host $1 -c 300 -w $dc-bond0-$1-$(date +"%s").pcap
}
alias TCPdump='/ghostcache/socc/jporras/tcpdump.sh'
alias out='tcpdump -nni bond0 -S -s0 -c 500 dst host '
alias in='tcpdump -nni bond1 -S -s0 -c 500 dst host '
alias bb='tail -f -n 1000 /ghostcache/logs/bb-ip-auth.log'
alias bl='tail -f -n 1000 /ghostcache/logs/all_bl.log'
alias clean='tcpdump -ttttnni bond0'
alias dirty='tcpdump -ttttnni bond1'
alias logs='cd /ghostcache/logs/'
alias pacman='tail -f -n 1000 /ghostcache/logs/bb-acl.log'
alias pcap1='tcpdump -ttttnnr'
alias pcap='TZ=UTC tcpdump -ttttnnr'
alias snort='tail -f -n 1000 /ghostcache/logs/all_snort.log'
alias source='tcpdump -nni bond1 -S -s0 -c 1500 src host '
alias sudo='echo '\''Running command without sudo'\'';'
alias taildpro='tail -f -n 1000 /ghostcache/logs/dpro.log'
alias inv='tcpdump -nni bond0 -S -s0 -c 200 dst net '
alias outv='tcpdump -nni bond1 -S -s0 -c 200 dst net '
alias time='export TMime43200'
