# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yitani <yitani@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/13 13:00:00 by yitani            #+#    #+#              #
#    Updated: 2025/11/15 12:31:15 by yitani           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

up:
	docker-compose up -d --build

down:
	docker-compose down

clean:
	docker-compose down -v

fclean:
	docker-compose down -v --rmi all

re: fclean up

logs:
	docker-compose logs -f

ps:
	docker-compose ps

.PHONY: up down clean fclean re logs ps