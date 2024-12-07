#!/bin/bash
COMPOSE="docker-compose -f ../backend/backend.yaml -f ../backend/nginx.yaml"
COMPOSE_UP="$COMPOSE up -d"

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
CYAN=$(tput setaf 6)
NC=$(tput sgr0)

echo "${YELLOW}1 = build${NC}"
echo "${GREEN}2 = up${NC}"
echo "${CYAN}3 = stop${NC}"
echo "${RED}4 = down${NC}"

read -n 1 -p 'whad do do? ' todo && echo

case $todo in
    1)
        echo && read -p "${RED}bildit'? (yeah=1)${NC} " -n 1 confirm && echo
        case $confirm in
            1) echo "${GREEN}building...${NC}" && $COMPOSE_UP --build;;
            *) echo "${YELLOW}atmenyau build${NC}";;
        esac
        ;;
    2) echo "${GREEN}podnimayu...${NC}" && $COMPOSE_UP;;
    3) echo "${GREEN}stopayu...${NC}" && $COMPOSE stop;;
    4) echo "${RED}popuskayu...${NC}" && $COMPOSE down;;
    *) echo "${CYAN}net such varianta, genius${NC}";;
esac
