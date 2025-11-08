/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   source.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yitani <yitani@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 22:19:22 by yitani            #+#    #+#             */
/*   Updated: 2025/11/07 22:33:54 by yitani           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <string.h>

int main(void)
{
	char input[1024];
	printf("please enter key: ");
	scanf("%s", input);
	if (strcmp(input, "__stack_check") == 0)
		printf("Good job.");
	else
		printf("Nope.");
}